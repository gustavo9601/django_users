from django.urls import path
from . import views

app_name = 'users_app'

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('logout/', views.LogoutUserView.as_view(), name='logout'),
    path('update-password/', views.UpdatePasswordUserView.as_view(), name='update_password'),
    path('code-verification/<pk>/', views.CodeVerificationUserView.as_view(), name='confirmation_code'),
]
