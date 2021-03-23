from django.urls import include, path
from posts.api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'posts', views.PostAPIView)

urlpatterns = [
    path('', include(router.urls)),
    path('posts/<int:pk>/like/', views.PostLikeAPIView.as_view(), name="homepage-post-like"),
    path('posts/<int:pk>/answer/', views.AnswerCreateAPIView.as_view(), name="answer-create"),
    path('posts/<int:pk>/answers/', views.AnswersListAPIView.as_view(), name="post-answers"),
    path('posts/<int:pk>/update/', views.UpdatePostDescriptionAPIView.as_view(), name="update-post"),
    path('answer/<int:pk>/', views.AnswerRUDAPIView.as_view(), name="answer-detail"),
]