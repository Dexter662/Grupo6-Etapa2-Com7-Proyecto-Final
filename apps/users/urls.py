from django.urls import path
from .views import user_list, user_admin_edit, user_detail, profile_edit, user_delete

app_name = 'users'

urlpatterns = [
    path('users/', user_list, name='list'),
    path('<int:pk>/', user_detail, name='detail'),
    path('<int:pk>/edit/', user_admin_edit, name='edit'),
    path('<int:pk>/delete/', user_delete, name='delete'),
    path('profile/edit/', profile_edit, name='profile_edit'),
]
