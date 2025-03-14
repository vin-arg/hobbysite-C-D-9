from django.shortcuts import render, get_object_or_404
from .models import Post, PostCategory

# Create your views here.
def thread_list(request):
    posts = Post.objects.all()  
    categories = PostCategory.objects.all()  
    return render(request, 'forum/thread_list.html', {'posts': posts, 'categories': categories})


def thread_detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    return render(request, 'forum/thread_detail.html', {'post': post})

def posts_by_category(request, category_id):
    category = get_object_or_404(PostCategory, id=category_id)
    posts = Post.objects.filter(category=category)
    return render(request, "forum/thread_list.html", {"posts": posts, "selected_category": category})