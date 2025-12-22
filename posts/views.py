from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post
from django.http import HttpResponse
from django.conf import settings

def test_storage(request):
    return HttpResponse(
        f"default={settings.DEFAULT_FILE_STORAGE}, "
        f"key={settings.AWS_SECRET_ACCESS_KEY}, "
        f"url={settings.AWS_S3_ENDPOINT_URL}"
    )

def create_post(request):
    if request.method == 'POST': # If user submits form
        form = PostForm(request.POST, request.FILES) # form object is created and .POST text is transferred and .FILES images too
        if form.is_valid():
            post = form.save(commit=False) # Saves the form into memory but not onto database, waiting for author
            post.author = request.user
            post.save()
            return redirect('posts_list')  
    else: 
        form = PostForm()
    
    return render(request, 'posts/create_post.html', {'form': form})


def posts_list(request):
    posts = Post.objects.all().order_by('-created_at') # The array of post objects ordered by newly created
    return render(request, 'posts/posts_list.html', {'posts': posts}) #{'posts': [posts]} passes the post to the template somehow

def post_detail(request, slug): # pk is primary key which links to "id" column in post table which is set by default by Django
    post = get_object_or_404(Post, slug=slug) # Fetches post according to id
    return render(request, 'posts/post_detail.html', {'post': post}) # Returns webpage to viewer with "post" object embedded into template


def home(request):
    latest_posts = Post.objects.order_by('-created_at')[:3]
    placeholder_range = [1, 2, 3]
    return render(request, 'index.html', {'latest_posts': latest_posts, 'placeholder_range': placeholder_range})

def employers(request):
    return render(request, "employers.html")