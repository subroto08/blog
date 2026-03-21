from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import blog, Category

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