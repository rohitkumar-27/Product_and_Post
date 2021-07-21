from django.urls import path
from .views import signup, posts_view, login_view, logout_view, post_create, post_edit, post_delete

urlpatterns = [
    path('', signup, name='signup'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('home', posts_view, name='home'),
    path('post_create', post_create, name='post_create'),
    path('home/<int:pk>/edit', post_edit, name='post_edit'),
    path('home/<int:pk>/delete', post_delete, name='post_delete'),


]