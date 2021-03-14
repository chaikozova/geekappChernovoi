from django.urls import path

from user import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('user-list', views.UserListView.as_view(), name='user-list'),
    path('password-reset/', views.reset_user_password, name='password-reset'),
    path('user/<int:pk>', views.UserRetrieveUpdateDeleteAPIView.as_view(
        {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update',
         'delete': 'destroy'}), name='user'),
]