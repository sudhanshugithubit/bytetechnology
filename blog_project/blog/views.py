# blog/views.py
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

class PostListCreateView(generics.ListCreateAPIView):    # Create
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    

class PostRetrieveView(generics.RetrieveAPIView): #Read
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class PostUpdateView(generics.UpdateAPIView):    #Update
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class PostDeleteView(generics.DestroyAPIView):    #Delete
    queryset = Post.objects.all()
    serializer_class = PostSerializer    
    

