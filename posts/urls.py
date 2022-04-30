from django.urls import path

from . import views

urlpatterns = [
    path('posts/', views.PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', views.PostRemove.as_view(), name='post-remove'),
    path('vote/<int:pk>/', views.VoteView.as_view(), name='vote-view')
]
