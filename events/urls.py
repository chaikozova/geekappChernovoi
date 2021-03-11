from django.urls import path
from events import views

urlpatterns = [
    path('api/v1/events/', views.EventAPIView.as_view()),
    path('api/v1/events/<int:id>/', views.EventDetailAPIView.as_view()),
]
