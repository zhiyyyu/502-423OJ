from django.urls import path

from user_info.admin_views import (AdminGetUserInfoList, AdminGetUserInfoByUsername, 
                                AdminUpdateUserInfo, AdminManagerUser, )
from user_info.user_views import (UserRegisterView, UserLoginView,
                                UserUploadAvatar, UserChangePassword,
                                UserResetEmail, GetUserResetPasswordToken,
                                UserResetPassword, GetUserResetEmailToken,
                                GetUsereProfile, )

urlpatterns = [
    # admin_view
    path('admin/user_info/', AdminGetUserInfoList.as_view(), name='user_info'),
    path('admin/user_info_by_username/', AdminGetUserInfoByUsername.as_view(), name='user_info_by_name'),
    path('admin/update_user_info/', AdminUpdateUserInfo.as_view(), name='update_user_info'),
    path('admin/user/', AdminManagerUser.as_view(), name='user'),
    # user_view
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('avatar/', UserUploadAvatar.as_view(), name='upload_avatar'),
    path('change_password/', UserChangePassword.as_view(), name='user_change_password'),
    path('reset_pwd_token/', GetUserResetPasswordToken.as_view(), name='user_reset_pwd_token'),
    path('reset_pwd/', UserResetPassword.as_view(), name='user_reset_pws'),
    path('reset_email_token/', GetUserResetEmailToken.as_view(), name='user_reset_email_token'),
    path('reset_email/', UserResetEmail.as_view(), name='user_reset_email'),
    path('profile/', GetUsereProfile.as_view(), name='user_profile'),
]