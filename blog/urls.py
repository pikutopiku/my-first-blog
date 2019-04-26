from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('past/<int:pk>/', views.post_detail, name='post_detail')
]
