from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ['title', 'category','status','created_at', 'updated_at']
  list_filter = ['category','status']
  list_editable = ['category','status']