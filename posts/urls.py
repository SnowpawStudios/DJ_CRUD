
from django.urls import path
from .import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('create/', views.create_post, name = 'create'),
    path('post/<int:pk>/', views.detail_post, name = 'detail-post'),
    path('post/update/<int:pk>/', views.update_post, name='update-post'),
    path('post/delete/<int:pk>/', views.delete_post, name='delete-post'),
]