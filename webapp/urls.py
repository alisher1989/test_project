from django.urls import path

from webapp.views import IndexView, ProductView, UpdateProfileView, ChangePasswordView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('products/', ProductView.as_view({'get': 'list'})),
    path('update_profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
]