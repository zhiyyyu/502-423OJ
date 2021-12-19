import requests
import hashlib
import json
import logging
import django_redis
from django.db import transaction
import time
import subprocess
import os
import psutil
import sys
sys.path.append("../../")

from conf.global_conf import LANGUAGE_SRC_FILE, LANGUAGE_OUT_FILE, BUILD_CMD
# from user_info.models import User, UserProfile
from problemlist.models import Problem
from submission.models import Submission, JudgeStatus, Result, Usage
from judge.languages import languages

root = "./judge"

class Judger(object):

    def __init__(self, submission_id, problem_id):

        self.fin = open(os.path.join(root, 'a.in'), 'r+')
        self.fout = open(os.path.join(root, 'a.out'), 'w+')
        self.submission = Submission.objects.get(id=submission_id)
        self.problem = Problem.objects.get(id=problem_id)

    # def _request(self, data):
    #     try:
    #         res = requests.post(self.url, data=json.dumps(data), headers=self.headers).json()
    #         return res
    #     except Exception as e:
    #         return {'code': -999, 'msg': 'exception'}

    def _static_info_handler(self, data):
        info = {}
        info['time_cost'] = max([x['cpu_time'] for x in data])
        info['memory_cost'] = max([x['memory'] for x in data])
        self.submission.static_info = info

    def _compile_with(self, language):
        
        p = subprocess.Popen(BUILD_CMD[language],shell=True,cwd=root,stdin=self.fin,stdout=self.fout,stderr=subprocess.PIPE) #cwd设置工作目录
        err = p.communicate()#获取编译错误信息

        if p.returncode != 0: # 编译失败
            return False
        return True

    def _set_submission_status(self, result, score, return_code, usage_memory, usage_time):

        self.submission.result = result
        self.submission.info = Result.objects.create(
            score=score,
            error_code=0,
        )
        self.submission.static_info = Usage.objects.create(
            memory=usage_memory,
            time=usage_time,
        )
        self.submission.save()

    def _judge_result(self):
        '''对输出数据进行评测'''
        currect_result = os.path.join(root, "ans.out")
        user_result = os.path.join(root, "a.out")
        try:
            curr = open(currect_result).read().replace('\r','').rstrip()#删除\r,删除行末的空格和换行  
            print(curr)
            user = open(user_result).read().replace('\r','').rstrip()  #python2中使用file函数
            print(user)
        except:
            return False
        if curr == user:       #完全相同:AC
            return "Accepted"
        if curr.split() == user.split(): #除去空格,tab,换行相同:PE
            return "Presentation Error"
        if curr in user:  #输出多了
            return "Output limit"
        return "Wrong Answer"  #其他WA

    def judge(self):

        # 构造测评的data
        language = self.submission.language
        config = list(filter(lambda item: language == item["name"], languages))[0]
        code = self.submission.code
        data = {
            "src": code,
            "language_config": config['config'],
            "max_cpu_time": self.problem.time_limit,
            "max_memory": 1024 * self.problem.memory_limit,
            "test_case_id": str(self.problem.id),
            "output": False,
        }

        # 修改状态为测评中
        Submission.objects.filter(id=self.submission.id).update(result=JudgeStatus.JUDGING)
        
        # 提交测评
        # print("judger write.")
        resp = {
            'result':0,
            'err':True, 
        }
        with open(os.path.join(root, LANGUAGE_SRC_FILE[self.submission.language]), 'w+') as f:
            f.write(code)

        # print('start compile.')
        # resp['err'] = self._compile_with(self.submission.language)
        # print(resp['err'])
        max_rss = 0
        p = subprocess.Popen(BUILD_CMD[language],shell=True,cwd=root,stdin=self.fin,stdout=self.fout,stderr=subprocess.PIPE) #cwd设置工作目录
        start_time = time.time()
        print(p.returncode)

        # if p.returncode != 0:
        #     self._set_submission_status(JudgeStatus.COMPILE_ERROR, 0, p.returncode, 0, 0)
        #     self._update_user_statues_handler()
        #     return

        pid = p.pid
        glan = psutil.Process(pid) #监听控制进程
        
        while True:
            time_now = time.time() - start_time
            if psutil.pid_exists(pid) is False:   #运行错误
                self._set_submission_status(JudgeStatus.RUNTIME_ERROR, 0, p.returncode, max_rss/1024.0, time_now*1000)
                self._update_user_statues_handler()
                return

            rss = glan.memory_info()[0] #获取程序占用内存空间 rss
            if p.poll() == 0:  #运行正常结束，跳出循环，继续判断
                end = time.time() - start_time
                break
            if max_rss < rss:
                max_rss = rss
                
            if time_now > self.problem.time_limit/1000:  #时间超限
                self._set_submission_status(JudgeStatus.CPU_TIME_LIMIT_EXCEEDED, 0, p.returncode, max_rss/1024.0, time_now*1000)
                self._update_user_statues_handler()
                glan.terminate()
                return 
            if max_rss > self.problem.memory_limit*1024*1024: #内存超限
                self._set_submission_status(JudgeStatus.MEMORY_LIMIT_EXCEEDED, 0, p.returncode, max_rss/1024.0, time_now*1000)
                self._update_user_statues_handler()
                glan.terminate()
                return
                
        self._set_submission_status(JudgeStatus.ACCEPTED, 100, p.returncode, max_rss/1024.0, time_now*1000)
        self._update_user_statues_handler()
        return 

        # if resp['err']:
        #     print('CE!')
        #     self.submission.result = JudgeStatus.COMPILE_ERROR
        #     info = {'err_info': resp['data']}
        #     self.submission.static_info = info
        # else:
        #     resp['result'] = self._judge_result()
        #     print(resp['result'])
        #     if resp['result'] == 'Accepted':
        #         self.submission.result = JudgeStatus.ACCEPTED

            # resp["data"].sort(key=lambda x: int(x["test_case"]))
            # self.submission.info = resp
            # self._static_info_handler(resp['data'])
            # error_test_case = list(filter(lambda case: case["result"] != 0, resp["data"]))
            # if not error_test_case:
            #     self.submission.result = JudgeStatus.ACCEPTED
            # else:
            #     self.submission.result = error_test_case[0]["result"]

        # self.submission.save()
        # self._update_user_statues_handler()

    def _update_user_statues_handler(self):
        with transaction.atomic():
            self.problem.submission_number += 1
            if self.submission.result == JudgeStatus.ACCEPTED:
                self.problem.ac_number += 1
            self.problem.save()


# if __name__ == '__main__':

#     Judger(0, 0).judge()