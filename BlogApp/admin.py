from django.contrib import admin
from .models import BlogPost

# Register your models here.

admin.site.register(BlogPost)



# @admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')  # Columns displayed in admin list view
    search_fields = ('title', 'author')  # Add search functionality
    list_filter = ('created_at', 'updated_at')  # Add filtering by date
