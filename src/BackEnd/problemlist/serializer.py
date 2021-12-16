from rest_framework import serializers

from problemlist.models import Problem, Category, Tag, Avatar
from comment.serializer import CommentSerializer
from user_info.serializer import UserDescSerializer


class AvatarSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name='avatar-detail')

    class Meta:
        model = Avatar
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):

    # 检查是否有重复的标签
    def check_tag_obj_exists(self, validated_data):
        text = validated_data.get('text')
        if Tag.objects.filter(text=text).exists():
            raise serializers.ValidationError('Tag with text {} exists.'.format(text))

    # 
    def create(self, validated_data):
        self.check_tag_obj_exists(validated_data)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        self.check_tag_obj_exists(validated_data)
        return super().update(instance, validated_data)

    class Meta:
        model = Tag
        fields = '__all__'


class ProblemCategoryDetailSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name='problemlist-detail')

    class Meta:
        model = Problem
        fields = [
            'title',
            'url',
        ]


class CategoryDetailSerializer(serializers.ModelSerializer):
    # category的详情信息
    articles = ProblemCategoryDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = [
            'id',
            'title',
            'created',
            'articles',
        ]


class CategorySerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name='category-detail') # category-detail是rest_framework自动创建的详情页面

    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['created']


class ProblemListBaseSerializer(serializers.HyperlinkedModelSerializer):    # 自动提供外键字段的超链接

    # HyperlinkedModelSerializer自动链接了
    # url = serializers.HyperlinkedIdentityField(view_name='problemlist:detail')  # 表示是problemlist的namespace下的detail，跟path里一致
    # 绑定作者信息
    author = UserDescSerializer(read_only=True)
    # 绑定分类信息，通过嵌套的方式显示指定
    category = CategorySerializer(read_only=True)
    # category 的 id 字段，用于创建/更新 category 外键
    category_id = serializers.IntegerField(write_only=True, allow_null=True, required=False)
    # tag字段
    tags = serializers.SlugRelatedField(    # 没必要专门加个超链接，只用显示tags的text字段就行了
        queryset=Tag.objects.all(),
        many=True,
        required=False,
        slug_field='text'
    )
    # 图片字段
    avatar = AvatarSerializer(read_only=True)
    avatar_id = serializers.IntegerField(
        write_only=True, 
        allow_null=True, 
        required=False
    )

    # # category_id 字段的验证器
    # def validate_category_id(self, value):
    #     if not Category.objects.filter(id=value).exists() and value is not None:
    #         raise serializers.ValidationError("Category with id {} not exists.".format(value))
    #     return value

    # # 验证图片 id 是否存在
    # # 不存在则返回验证错误
    # def validate_avatar_id(self, value):
    #     if not Avatar.objects.filter(id=value).exists() and value is not None:
    #         raise serializers.ValidationError("Avatar with id {} not exists.".format(value))

    #     return value

    # 自定义错误信息
    default_error_messages = {
        'incorrect_avatar_id': 'Avatar with id {value} not exists.',
        'incorrect_category_id': 'Category with id {value} not exists.',
        'default': 'No more message here..'
    }

    def check_obj_exists_or_fail(self, model, value, message='default'):
        if not self.default_error_messages.get(message, None):
            message = 'default'

        if not model.objects.filter(id=value).exists() and value is not None:
            self.fail(message, value=value)

    def validate_avatar_id(self, value):
        self.check_obj_exists_or_fail(
            model=Avatar,
            value=value,
            message='incorrect_avatar_id'
        )

        return value

    def validate_category_id(self, value):
        self.check_obj_exists_or_fail(
            model=Category,
            value=value,
            message='incorrect_category_id'
        )

        return value
    
    # 覆写方法，如果输入的标签不存在则创建它
    def to_internal_value(self, data):
        tags_data = data.get('tags')

        if isinstance(tags_data, list):
            for text in tags_data:
                if not Tag.objects.filter(text=text).exists():
                    Tag.objects.create(text=text)

        return super().to_internal_value(data)
    
    class Meta:
        model = Problem
        fields = '__all__'


class ProblemListSerializer(ProblemListBaseSerializer):

    class Meta:
        model = Problem
        fileds = '__all__'
        extra_kwargs = {'body': {'write_only' :'True'}}
    

class ProblemDetailSerializer(ProblemListBaseSerializer):

    # 渲染后的正文
    body_html = serializers.SerializerMethodField()
    # 渲染后的目录
    toc_html = serializers.SerializerMethodField()
    # 题目的评论
    id = serializers.IntegerField(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    def get_body_html(self, obj):
        return obj.get_md()[0]

    def get_toc_html(self, obj):
        return obj.get_md()[1]
    
    class Meta:
        model = Problem
        fields = '__all__'