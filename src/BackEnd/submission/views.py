from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from problemlist.models import Problem
from user_info.models import UserType, UserProfile
from submission.models import Submission, Result, Usage
from submission.seriliazer import (UserSubmitCodeSerializer, UserGetSubmissionResultSerializer,
                                SubmissionSerializer, StatusSerializer,
                                ResultSerializer, UsageSerializer,
                                UserSubmissionListSerializer)
# from judge.tasks import judge
from judge.easy_judge import Judger
from utils.api import get_user_and_token_by_jwt_request


class ResultViewSet(viewsets.ModelViewSet):

    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    permission_classes = [AllowAny]


class UsageViewSet(viewsets.ModelViewSet):

    queryset = Usage.objects.all()
    serializer_class = UsageSerializer
    permission_classes = [AllowAny]


class StatusViewSet(viewsets.ModelViewSet):

    queryset = Submission.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [AllowAny]


class SubmissionListDetailViewSet(viewsets.ModelViewSet):

    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    permission_classes = [AllowAny]


# 用户提交代码
class SubmissionViewSet(viewsets.ModelViewSet):

    queryset = Submission.objects.all()
    serializer_class = UserSubmitCodeSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]

    def get_serializer_class(self):

        print('receive request.')
        if self.request.method == 'GET':
            serializer_class = UserGetSubmissionResultSerializer    

        elif self.request.method == 'POST':
            serializer_class = UserSubmitCodeSerializer

            # user, token = get_user_and_token_by_jwt_request(self.request)

            # if user:
            data = self.request.data
            print("user_id: ", self.request.user.id)
            submission = Submission.objects.create(
                                problem=Problem.objects.get(id=data['problem']),
                                user_id=self.request.user.id,
                                code=self.request.data['code'],
                                language=self.request.data['language'],
                                )
            # submission.save()
            # print('before judge delay.')
            Judger(submission.id, data['problem']).judge()
        
        return serializer_class


# 用户获取后端的结果
class SubmissionResultViewSet(viewsets.ModelViewSet):

    queryset = Submission.objects.all()
    serializer_class = UserGetSubmissionResultSerializer
    permission_classes = [AllowAny]

    # def get_serializer_class(self):

    #     if self.request.method == 'list':
    #         serializer_class = UserGetSubmissionResultSerializer
        
    #     else:
    #         serializer_class = 


class UserSubmissionListViewSet(viewsets.ModelViewSet):

    queryset = Submission.objects.all()
    serializer_class = UserSubmissionListSerializer
    permission_classes = [AllowAny]
