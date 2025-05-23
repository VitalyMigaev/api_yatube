from rest_framework import serializers

from posts.models import Comment, Group, Post


class BaseSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        abstract = True


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class PostSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Post
        fields = '__all__'


class CommentSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Comment
        fields = '__all__'
        read_only_fields = ('post',)
