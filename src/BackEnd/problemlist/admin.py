from django.contrib import admin
from .models import Problem, Tag


# Register your models here.
# 注册Problem APP，能在admin的网站中找到，并增加数据
admin.site.register(Problem)
admin.site.register(Tag)