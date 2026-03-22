from multiprocessing import context
from urllib import request
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import blog, Category
from django.db.models import Q

# Create your views here.
def posts_by_category(request, category_id):
   #fetch the posts that belong to the category with the category_id
   posts = blog.objects.filter(status='Published', category=category_id)
   #use try/except to handle the case where the category with the category_id does not exist
   try:
       category = Category.objects.get(pk=category_id) 
   except :
       #redirect to the user to the home page
       return redirect('home')
   
   #category = get_object_or_404(category, pk=category_id)
   context = {
      'posts': posts,
      'category': category,
   }
   return render(request, 'posts_by_category.html',context)

def blogs(request, slug):
    single_blog = get_object_or_404(blog, slug=slug, status='Published')
    context = {
        'single_blog': single_blog,
    }
    return render(request, 'blogs.html', context)


def search(request):
     keyword = request.GET.get('keyword')

     blogs = blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status='Published')
     context = {
            'blogs': blogs,
            'keyword': keyword,
     }
     return render(request, 'search.html', context) 