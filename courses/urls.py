from django.urls import path
from courses import views

urlpatterns = [
    path('api/v1/courses/', views.CourseAPIView.as_view()),
    path('api/v1/courses/<int:id>/', views.CourseDetailAPIView.as_view()),
    path('api/v1/levels/', views.LevelAPIView.as_view()),
    path('api/v1/levels/<int:id>/', views.LevelDetailAPIView.as_view()),
]