from django.db import models

# Create your models here.
class Post(models.Model):
  
  CATEGORY_CHOICES = (
    ("IT", "Technology"),
    ("PTG", "Photography"),
    ("LS", "Life styles")
  )
  
  title = models.CharField(max_length=255, blank=True)
  body = models.TextField()
  photo = models.ImageField(upload_to='blog/%Y/%m/%d', blank=True)
  category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
  status = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  class Meta:
    ordering = ['-created_at']

  def __str__(self):
    return self.title