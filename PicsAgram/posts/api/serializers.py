import locale
from posts.models import Answer, Post
from rest_framework import serializers

locale.setlocale(locale.LC_TIME, 'Italian_Italy')


class AnswerSerializer(serializers.ModelSerializer):
    
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)

    class Meta():
        model = Answer
        exclude = ["updated_at", "post"]

    def get_created_at(self, instance):
        return instance.created_at.strftime('%d %B %Y')


class PostSerializer(serializers.ModelSerializer):
    
    answers_count = serializers.SerializerMethodField(read_only=True)
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)
    user_has_liked = serializers.SerializerMethodField(read_only=True)
    likes_count = serializers.SerializerMethodField(read_only=True)

    class Meta():
        model = Post
        exclude = ["updated_at", "voters"]

    def get_created_at(self, instance):
        return instance.created_at.strftime('%d %B %Y')

    def get_user_has_liked(self, instance):
        request = self.context.get("request")
        return instance.voters.filter(pk=request.user.pk).exists()

    def get_likes_count(self, instance):
        return instance.voters.count()

    def get_answers_count(self, instance):
        return instance.answers.count()


class PostDescriptionSerializer(serializers.ModelSerializer):

    class Meta():
        model = Post
        fields = ["description"]