from django.shortcuts import render, get_object_or_404
from rest_framework import status
from .models import Post, Category
from .serializers import PostSerializer, PostListSerializer, CategorySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def category_list(request):
    # 모든 카테고리 정보를 요청자에게 넘겨준다.
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def post_list_create(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        category = Category.objects.get(pk=request.data.get('category'))
        if serializer.is_valid(raise_exception=True):
            serializer.save(category=category)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def post_detail(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    serializer = PostSerializer(post)
    return Response(serializer.data)


