from authentication.forms import LoginForm
from authentication.views import DashboardView
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path('', auth_views.LoginView.as_view(
        template_name='login.html',
        redirect_authenticated_user=True,
        authentication_form=LoginForm
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='login.html'), name='logout'),
    path('dashboard/', DashboardView.as_view(), name='dashboard')
]
