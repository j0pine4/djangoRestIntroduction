from django.db.models import query
from django.db.models.query import QuerySet
from rest_framework import generics
from blog.models import *
from .serializers import *

# Create your views here.
class PostList(generics.ListCreateAPIView):
    queryset = Post.postObjects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer