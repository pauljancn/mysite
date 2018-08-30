from django.contrib import admin
from suanpi.models import BlogPost

# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title','body','timestamp']
    
admin.site.register(BlogPost,BlogPostAdmin)