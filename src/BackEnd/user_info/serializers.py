from django import forms
from rest_framework import serializers

from user_info.models import UserProfile


# 用户注册表单
class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, min_length=6, max_length=150)
    password = serializers.CharField(required=True, min_length=6, max_length=150)
    passwordagain = serializers.CharField(required=True, min_length=6, max_length=150)
    # nickname = serializers.CharField(required=True, min_length=6)
    email = serializers.EmailField(required=True)
 

# 用户登陆表单
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, min_length=6, max_length=150)
    password = serializers.CharField(required=True, min_length=6, max_length=150)


# 上传图片
class ImageUploadForm(forms.Form):
    image = forms.FileField()


# 更改密码
class UserChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True, min_length=6, max_length=150)
    new_password = serializers.CharField(required=True, min_length=6, max_length=150)


class GetUserResetPasswordTokenSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, min_length=6, max_length=150)


class UserResetPasswordSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, min_length=6, max_length=150)
    token = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, min_length=6, max_length=150)


# 重置邮箱
class GetUserResetEmailTokenSerializer(serializers.Serializer):
    op_type = serializers.CharField(required=True)
    new_email = serializers.EmailField(required=True)


class UserResetEmailSerializer(serializers.Serializer):
    new_email = serializers.EmailField(required=True)
    token = serializers.CharField(required=True)


# 更改用户画像
class UpdateUserProfleSerializer(serializers.Serializer):
    nickname = serializers.CharField(required=False, min_length=6)
    motto = serializers.CharField(required=False)


# 获取用户信息
class AdminManagerUserInfoSerializer(serializers.Serializer):
    id = serializers.IntegerField(source='user.id')
    username = serializers.CharField(source='user.username')
    nickname = serializers.CharField()
    email = serializers.EmailField(source='user.email')
    user_type = serializers.CharField(source='user.user_type')


class AdminUpdateUserInfoSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, min_length=6, max_length=150)
    nickname = serializers.CharField(required=True, min_length=6, max_length=150)
    password = serializers.CharField(required=False, min_length=6, max_length=150)
    email = serializers.EmailField(required=True)
    user_type = serializers.CharField(required=True)


class AdminGetUserInfoByUsernameSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, min_length=6, max_length=150)


class AdminAddUserSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, min_length=6, max_length=150)
    nickname = serializers.CharField(required=True, min_length=6, max_length=150)
    password = serializers.CharField(required=True, min_length=6, max_length=150)
    email = serializers.EmailField(required=True)
    user_type = serializers.CharField(required=True)


class AdminDeleteUserSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, min_length=6, max_length=150)


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = "__all__"