from django.shortcuts import render, get_list_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

class BlogListView(APIView):
    def get(self, request, *arg, **kwargs):
        posts = Post.objects.all()[0:4]
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
class PostDetailView(APIView):
    def get(self, request, *arg, **kwargs):
        post_slug = self.kwargs.get('slug')
        post = get_list_or_404(Post, slug=post_slug)
        serializer = PostSerializer(post)
        return Response(serializer.data)