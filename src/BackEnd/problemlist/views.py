from rest_framework.decorators import api_view, APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status, viewsets, generics
from django.http import Http404

from problemlist.models import Problem, Category, Tag, Avatar
from problemlist.serializer import (ProblemListSerializer, ProblemDetailSerializer, 
                                CategorySerializer, CategoryDetailSerializer,
                                TagSerializer, 
                                AvatarSerializer
                                )
from problemlist.permission import IsAdminUserOrElseReadOnly

# Create your views here.
# @api_view(['GET', 'POST'])
# def problem_list(request):

#     if request.method == 'GET':
#         problems = Problem.objects.all()
#         serializer = ProblemListSerializer(problems, many=True, context={'request':request})
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = ProblemListSerializer(data=request.data, context={'request':request})

#         if not serializer.is_valid():
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


class AvatarViewSet(viewsets.ModelViewSet):

    queryset = Avatar.objects.all()
    serializer_class = AvatarSerializer
    permission_classes = [IsAdminUserOrElseReadOnly]


class TagViewSet(viewsets.ModelViewSet):

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminUserOrElseReadOnly]


class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrElseReadOnly]

    def get_serializer_class(self):
        # 只是查看category列表
        if self.action == 'list':
            return CategorySerializer
        # 查看category的详情
        else:
            return CategoryDetailSerializer


# 题目列表视图
class ProblemListViewSet(viewsets.ModelViewSet):

    queryset = Problem.objects.all()
    serializer_class = ProblemListSerializer
    # 管理员可写，所有人可读
    permission_classes = [IsAdminUserOrElseReadOnly]
    # 过滤字段
    filterset_fields = ['author__username', 'title']

    # 往序列化数据中添加从request获得的用户信息
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # 过滤文章，只看制定User的文章
    def get_queryset(self):
        queryset = self.queryset
        username = self.request.query_params.get('username', None)

        if username is not None:
            queryset = queryset.filter(author__username=username)

        return queryset

    def get_serializer_class(self):
        # 列表界面
        if self.action == 'list':
            return ProblemListSerializer
        # 详情界面
        else:
            return ProblemDetailSerializer


# 单个题目的详细描述
class ProblemDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Problem.objects.all()
    serializer_class = ProblemDetailSerializer
    permission_classes = [IsAdminUserOrElseReadOnly]



    # # 获取单个对象
    # # pk即主键，默认是id
    # def get_object(self, pk):
        
    #     try:
    #         return Problem.objects.get(pk=pk)
    #     except:
    #         raise Http404

    # def get(self, request, pk):

    #     problem = self.get_object(pk)
    #     serializer = ProblemDetailSerializer(problem)
    #     return Response(serializer.data)

    # def put(self, request, pk):

    #     problem = self.get_object(pk)
    #     serializer = ProblemDetailSerializer(problem)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # def delete(self, request, pk):

    #     problem = self.get_object(pk)
    #     problem.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
