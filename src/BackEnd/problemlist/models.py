from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from markdown import Markdown

# Create your models here.

class Category(models.Model):
    # 题目所属的题集
    title = models.CharField(max_length=100)
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class Tag(models.Model):

    text = models.CharField(max_length=30)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.text


class Avatar(models.Model):

    content = models.ImageField(upload_to='avatar/%Y%m%d')


class Problem(models.Model):

    # 标题
    title = models.CharField(max_length=100)
    # 正文，包括输入输出数据等
    body = models.TextField()
    # 创建时间
    created = models.DateTimeField(default=timezone.now)
    # 作者，每道题对应一个作者
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE, 
        related_name='problemlist'
    )
    # 分类，可以用作题集
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='problemlist'
    )
    # 标签，题目用到的方法标签
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name='problemlist',
    )
    # 标题图
    avatar = models.ForeignKey(
        Avatar,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='problemlist',
    )

    # body字段使用markdown渲染
    def get_md(self):
        md = Markdown(
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
            ]
        )
        md_body = md.convert(self.body)
        # toc 是渲染后的目录
        return md_body, md.toc

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']
