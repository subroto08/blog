from django.contrib import admin

from blogs.models import Category, blog

class blogAdmin(admin.ModelAdmin):
   prepopulated_fields = {'slug':('title',)}
   list_display = ('title', 'author', 'category', 'is_featured', 'status',)
   search_fields = ('id', 'title', 'category__category_name', 'status')
   list_editable = ('is_featured',)

admin.site.register(Category)

admin.site.register(blog, blogAdmin)
