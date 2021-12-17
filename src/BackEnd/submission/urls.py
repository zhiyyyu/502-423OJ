from django.urls import path, include
from submission.views import SubmissionAPI

app_name = 'submission'

urlpatterns = [
    # path('', submission_list, name='list'),
    # path('<int:pk>/', SubmissionAPI.as_view(), name='detail'), # <int:pk> 是路径转换器
]