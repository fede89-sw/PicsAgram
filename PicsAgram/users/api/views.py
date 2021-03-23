from .permissions import IsOwnerOrReadOnly
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import DetailUserSerializer, RetriveUserSerializer, ProfilePictureSerializer, UserThemeSerializer
from users.models import CustomUser


class RetriveUserAPIView(generics.RetrieveAPIView):

    serializer_class = RetriveUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class DetailUserAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = CustomUser.objects.all()
    serializer_class = DetailUserSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    lookup_field = "username"


class ProfilePictureUpdateView(generics.UpdateAPIView):
    serializer_class = ProfilePictureSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        profile_object = self.request.user
        return profile_object


class UserThemeUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = UserThemeSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_object(self):
        profile_object = self.request.user
        return profile_object