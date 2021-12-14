from rest_framework import viewsets
from account.models import User
from account.serializer import UserSerializer


# 对User进行增删查改
class UserViewSets(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer