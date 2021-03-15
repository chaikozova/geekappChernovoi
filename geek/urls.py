"""geek URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users import views as user_views
from courses import views as courses_views
from events import views as events_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', user_views.LoginView.as_view(), name='login'),
    path('api/logout/', user_views.LogoutView.as_view(), name='logout'),
    path('api/user-create/', user_views.UserRegistrationView.as_view(), name='user-create'),
    path('api/courses/', courses_views.CourseAPIView.as_view()),
    path('api/courses/<int:id>/', courses_views.CourseDetailAPIView.as_view()),
    path('api/levels/', courses_views.LevelAPIView.as_view()),
    path('api/levels/<int:id>/', courses_views.LevelDetailAPIView.as_view()),
    path('api/events/', events_views.EventAPIView.as_view()),
    path('api/events/<int:id>/', events_views.EventDetailAPIView.as_view()),
]
