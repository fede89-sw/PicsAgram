from rest_framework import serializers
from users.models import CustomUser
from posts.api.serializers import PostSerializer

class DetailUserSerializer(serializers.ModelSerializer):

    posts = PostSerializer(many=True, read_only=True)
    profile_picture = serializers.ImageField(read_only=True)

    class Meta():
        model = CustomUser
        fields = ["username", "first_name", "last_name",
                  "email", "biography", "profile_picture",
                  "posts"]


class RetriveUserSerializer(serializers.ModelSerializer):

    class Meta():
        model = CustomUser
        fields = ["username"]


class ProfilePictureSerializer(serializers.ModelSerializer):

    class Meta():
        model = CustomUser
        fields = ["profile_picture",]


class UserThemeSerializer(serializers.ModelSerializer):

    class Meta():
        model = CustomUser
        fields = ["theme",]