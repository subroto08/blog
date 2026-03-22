
from django.shortcuts import render

from assignments.models import About
from blogs.models import blog, Category 

def home(request):
    featured_posts = blog.objects.filter(is_featured=True, status='Published').order_by('-updated_at')
    posts = blog.objects.filter(is_featured=False, status='Published')

    #fetch about us
    try:
        about = About.objects.get()
    except:
        about = None
    context = {
        'featured_posts': featured_posts,
        'posts': posts,
        'about': about,

    }
    return render(request, 'home.html', context)