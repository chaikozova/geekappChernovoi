from django.urls import path
from . import views as courses_views

urlpatterns = [
    path('api/courses/', courses_views.CourseAPIView.as_view()),
    path('api/courses/<int:id>/', courses_views.CourseDetailAPIView.as_view()),
    path('api/levels/', courses_views.LevelAPIView.as_view()),
    path('api/levels/<int:id>/', courses_views.LevelDetailAPIView.as_view()),

]