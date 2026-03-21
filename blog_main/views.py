
from django.shortcuts import render

from blogs.models import blog, Category 

def home(request):
    featured_posts = blog.objects.filter(is_featured=True, status='Published').order_by('-updated_at')
    posts = blog.objects.filter(is_featured=False, status='Published')
    context = {
        'featured_posts': featured_posts,
        'posts': posts,

    }
    return render(request, 'home.html', context)