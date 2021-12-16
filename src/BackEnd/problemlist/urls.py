from django.urls import path, include

# from problemlist.views import problem_list
from problemlist.views import ProblemDetail

app_name = 'problemlist'

urlpatterns = [
    # path('', problem_list, name='list'),
    # path('<int:pk>/', ProblemDetail.as_view(), name='detail'), # <int:pk> 是路径转换器
]