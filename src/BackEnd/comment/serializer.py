from rest_framework import serializers

from comment.models import Comment
from user_info.serializers import AdminManagerUserInfoSerializer


class CommentChildrenSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='comment-detail')
    author = AdminManagerUserInfoSerializer(read_only=True)

    class Meta:
        model = Comment
        exclude = [
            'parent',
            'article'
        ]


class CommentSerializer(serializers.ModelSerializer):
    # 评论详情链接
    url = serializers.HyperlinkedIdentityField(view_name='comment-detail')
    # 作者信息
    author = AdminManagerUserInfoSerializer(read_only=True)

    # 问题链接
    problem = serializers.HyperlinkedRelatedField(view_name='problemlist-detail', read_only=True)
    problem_id = serializers.IntegerField(write_only=True, allow_null=False, required=True)

    # 父评论
    parent = CommentChildrenSerializer(read_only=True)
    parent_id = serializers.IntegerField(write_only=True, allow_null=True, required=False)

    def update(self, instance, validated_data):
        validated_data.pop('parent_id', None)
        return super().update(instance, validated_data)

    class Meta:
        model = Comment
        fields = '__all__'
        extra_kwargs = {'created': {'read_only': True}}