from django.shortcuts import render, get_object+or_404
from .models import Post

def post_list(request):
    posts = Post.objects.all() #fetch all post form database
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk) #fetch post by primary key(pk)
    return render(request, 'blog/post_detail.html', {'post': post})
