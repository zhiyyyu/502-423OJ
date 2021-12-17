from __future__ import absolute_import, unicode_literals
from BackEnd.celery import app
from celery import shared_task
from judge.judgehandler import JudgeHandler

@app.task
def judge(submission_id, problem_id):
    JudgeHandler(submission_id, problem_id).judge()

# @app.task
# def battle_judge(data):
#     return BattleJudgeHandler(data).judge()