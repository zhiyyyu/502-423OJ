from rest_framework import serializers

from user_info.serializers import AdminManagerUserInfoSerializer
from problemlist.serializer import ProblemListSerializer
from submission.models import Submission, Result, Usage


# 提交的代码运行所用的时空消耗
class UsageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usage
        fields = '__all__'


# 提交的得分和错误码
class ResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = Result
        fields = '__all__'


# 后端返回提交状态
class StatusSerializer(serializers.ModelSerializer):

    static_info = UsageSerializer(read_only=True)

    class Meta:
        model = Submission
        fields = [
            'submit_time',
            'user_id',
            'problem',
            'result',
            'static_info',
        ]


# 用户提交代码
class UserSubmitCodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Submission
        fields = [
            'problem',
            'user_id',
            'code',
            'language',
        ]


# 用户获取后端结果
class UserGetSubmissionResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = Submission
        fields = [
            'id',
            'info',
            'static_info',
        ]


class SubmissionSerializer(serializers.ModelSerializer):

    info = ResultSerializer()
    static_info = UsageSerializer()
    problem = ProblemListSerializer()

    class Meta:
        model = Submission
        fields = '__all__'