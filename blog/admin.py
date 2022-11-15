from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
  list_display = ['title', 'category','status','created_at', 'updated_at']
  list_filter = ['category','status']
  list_editable = ['category','status']
  summernote_fields = ('body',)