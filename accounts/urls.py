from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register_view, UserDetailView, UserPasswordChangeView, activate

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', register_view, name='create'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('<int:pk>/', UserDetailView.as_view(), name='detail'),
    path('<int:pk>/password_change', UserPasswordChangeView.as_view(), name='password_change'),
]
