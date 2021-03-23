from django.urls import path
from .views import DetailUserAPIView,ProfilePictureUpdateView, RetriveUserAPIView, UserThemeUpdateView


urlpatterns = [
    path('user/', RetriveUserAPIView.as_view(), name="logged-user"),
    path('<str:username>/', DetailUserAPIView.as_view(), name="user-info"),
    path('<str:username>/profile-picture/', ProfilePictureUpdateView.as_view(), name="user-picture"),
    path('<str:username>/theme/', UserThemeUpdateView.as_view(), name="user-theme")
]