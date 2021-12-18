from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from problemlist.models import Problem
from user_info.models import UserType
from submission.models import Submission, Result, Usage
from submission.seriliazer import (UserSubmitCodeSerializer, UserGetSubmissionResultSerializer,
                                SubmissionSerializer, StatusSerializer,
                                ResultSerializer, UsageSerializer)
from judge.tasks import judge
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
            submission = Submission.objects.create(
                                problem=Problem.objects.get(id=data['problem']),
                                user_id=self.request.user.id,
                                code=self.request.data['code'],
                                language=self.request.data['language'],
                                )
            submission.save()
            print('judging')
            judge.delay(submission.id, data['problem'])
        
        return serializer_class


# 用户获取后端的结果
class SubmissionResultViewSet(viewsets.ModelViewSet):

    queryset = Submission.objects.all()
    serializer_class = UserGetSubmissionResultSerializer
    permission_classes = [AllowAny]


class SubmissionAPI(APIView):

    permission_classes = [AllowAny]

    # # 接受前端的提交，向判题机发送代码
    # def post(self, request, *args, **kwargs):
    #     resp_data = {'code': 0, 'msg': 'success', 'data': {}}

    #     # print(request.data)
    #     serializer = UserSubmitCodeSerializer(data=request.data)
    #     if not serializer.is_valid():
    #         resp_data['code'] = -1
    #         resp_data['msg'] = 'request data error'
    #         return Response(data=resp_data)
        
    #     # print(serializer.data)
    #     pro_id = serializer.data['problem']
    #     try:
    #         problem = Problem.objects.get(id=pro_id)
    #     except Problem.DoesNotExist:
    #         resp_data['code'] = -2
    #         resp_data['msg'] = f"{pro_id} problem does not exist"
    #         return Response(data=resp_data)

    #     # user, token = JWTAuthentication().authenticate(request=request)

    #     # if (user.user_type == UserType.REGULAR_USER) and (not pro.visible):
    #     #     resp_data['code'] = -3
    #     #     resp_data['msg'] = 'no authority'
    #     #     return Response(data=resp_data)

    #     submission = Submission.objects.create(
    #                                             problem=problem,
    #                                             user_id=serializer.data['user_id'],
    #                                             code=serializer.data['code'],
    #                                             language=serializer.data['language'],
    #                                             )
    #     submission.save()
    #     judge.delay(submission.id, pro_id)
    #     resp_data['data']['submission_id'] = submission.id
    #     return Response(data=resp_data)

    # # 通过查看提交结果的请求来返回结果
    # def get(self, request):
    #     resp_data = {'code': 0, 'msg': 'success', 'data': {}}

    #     serializer = UserGetSubmissionResultSerializer(data=Submission)

    #     # not valid data
    #     if not serializer.is_valid():
    #         resp_data['code'] = -1
    #         resp_data['msg'] = 'request data error'
    #         return Response(data=resp_data)

    #     # print(serializer.data)
    #     submission_id = serializer.data['id']
    #     try:
    #         submission = Submission.objects.get(id=submission_id)   # 查找id是submission_id的提交
    #     except Submission.DoesNotExist:
    #         resp_data['code'] = -2
    #         resp_data['msg'] = f"{submission_id} submission does not exist"
    #         return Response(data=resp_data)

    #     # user, token = JWTAuthentication().authenticate(request=request)
    #     # if (user.id != submission.user_id) and (user.user_type != UserType.ADMIN_USER):
    #     #     resp_data['code'] = -3
    #     #     resp_data['msg'] = 'no authority'
    #     #     return Response(data=resp_data)

    #     resp_data['data'] = serializer.data
    #     return Response(data=resp_data)