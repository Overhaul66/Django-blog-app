from django.db import models
from django.urls import reverse
# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=100)
  
  author = models.ForeignKey(
    'Author',
    on_delete = models.CASCADE
  )
    
  content = models.TextField()
  
  def __str__(self):
    return self.title
    
  def get_absolute_url(self):
    return reverse("post", args=[str(self.id)])
    
class Author(models.Model):
  name = models.CharField(max_length=100)
  
  def __str__(self):
    return self.name[:50]