# created alone.

from django.urls import path
from .views import posts_list
from . import views

urlpatterns = [
    path('', posts_list, name="posts_list"),
    path('<slug:slug>/', views.post_detail, name="post_detail"),
    path('test-storage/', views.test_storage),
    
]

