from rest_framework import serializers

from user_info.serializer import UserDescSerializer
from problemlist.serializer import ProblemListSerializer
from submission.models import Submission, Result, Usage


class UsageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usage
        fields = '__all__'


class ResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = Result
        fields = '__all__'


class StatusSerializer(serializers.ModelSerializer):

    static_info = UsageSerializer()

    class Meta:
        model = Submission
        fields = [
            'submit_time',
            'user_id',
            'problem',
            'result',
            'static_info',
        ]


class UserSubmitCodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Submission
        fields = [
            'problem',
            'user_id',
            'code',
            'language',
        ]


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