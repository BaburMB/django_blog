from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.contrib.auth.models import User

def post_list(request):
    now = timezone.now()
    me = User.objects.get(username='bmb')
    posts = Post.objects.filter(author = me).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})



