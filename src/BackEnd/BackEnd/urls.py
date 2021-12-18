"""BackEnd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView, TokenVerifyView

from problemlist.views import ProblemListViewSet, TagViewSet
from comment.views import CommentViewSet
from submission.views import (SubmissionViewSet, SubmissionResultViewSet,
                            SubmissionListDetailViewSet,
                            ResultViewSet, UsageViewSet,
                            StatusViewSet)

router = DefaultRouter()
# 题库功能
router.register(r'problemlist', ProblemListViewSet)
# router.register(r'tag', TagViewSet)
# router.register(r'comment', CommentViewSet)
# # 用户登陆注册
# router.register(r'user', UserViewSet)
# 提交功能
# router.register(r'result', ResultViewSet)
# router.register(r'usage', UsageViewSet)
router.register(r'submission', SubmissionViewSet)
router.register(r'submission_detail', SubmissionListDetailViewSet)
router.register(r'submission_result', SubmissionResultViewSet)
router.register(r'submission_status', StatusViewSet)

urlpatterns = [
    # 后台url
    path('admin/', admin.site.urls),
    # # 登陆界面
    # path('api-auth/', include('rest_framework.urls')),
    # app的url
    path('api/', include('user_info.urls')),
    # path('api/submission/', include('submission.urls', namespace='submission')),   # namespace -> app_name
    path('api/', include(router.urls)),
    # JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    