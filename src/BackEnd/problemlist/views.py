from rest_framework.decorators import api_view
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from problemlist.models import Problem
from problemlist.serializer import ProblemSerializer
from problemlist.serializer import ProblemDetailsSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def problem_list(request):

    if request.method == 'GET':
        problems = Problem.objects.all()
        serializer = ProblemSerializer(problems, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProblemSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 单个题目的详细描述
class ProblemDetails(APIView):

    # 获取单个对象
    # pk即主键，默认是id
    def get_object(self, pk):
        
        try:
            return Problem.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk):

        problem = self.get_object(pk)
        serializer = ProblemDetailsSerializer(problem)
        return Response(serializer.data)

    def put(self, request, pk):

        problem = self.get_object(pk)
        serializer = ProblemDetailsSerializer(problem)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):

        problem = self.get_object(pk)
        problem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
