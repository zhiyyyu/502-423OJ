from django.db import models

from problemlist.models import Problem

# Create your models here.

class JudgeStatus(object):
    COMPILE_ERROR = -2
    WRONG_ANSWER = -1
    ACCEPTED = 0
    CPU_TIME_LIMIT_EXCEEDED = 1
    REAL_TIME_LIMIT_EXCEEDED = 2
    MEMORY_LIMIT_EXCEEDED = 3
    RUNTIME_ERROR = 4
    SYSTEM_ERROR = 5
    PENDING = 6
    JUDGING = 7
    PARTIALLY_ACCEPTED = 8

class Language(object):
    CPP = 0
    C = 1
    JAVA = 2
    PYTHON = 3


class Result(models.Model):

    error_code = models.IntegerField()
    score = models.IntegerField()

    class Meta:
        ordering = ['id']


class Usage(models.Model):

    time = models.IntegerField()
    memory = models.IntegerField()

    

class Submission(models.Model):
    # 提交的编号，主键
    id = models.BigAutoField(primary_key=True)
    # 提交的题目
    problem = models.ForeignKey(
        Problem,
        on_delete=models.CASCADE
    )
    # 提交的用户
    user_id = models.IntegerField(default=0)
    # 创建时间
    submit_time = models.DateTimeField(auto_now_add=True)
    # 提交代码
    code = models.TextField()
    # 提交结果
    result = models.IntegerField(db_index=True, default=JudgeStatus.PENDING)
    # Judge 返回的信息
    info = models.ForeignKey(
        Result,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='submission',
    )
    # 用时, 内存
    static_info = models.ForeignKey(
        Usage,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='submission',
    )
    # 使用的语言
    language = models.TextField(default=Language.CPP)



