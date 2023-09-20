# blog/urls.py
from django.urls import path
from .views import PostListCreateView
from .views import PostRetrieveView
from .views import PostUpdateView
from .views import PostDeleteView

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostRetrieveView.as_view(), name='post-retrieve'),
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
