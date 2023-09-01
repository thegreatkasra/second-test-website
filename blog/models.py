from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse                                                 #sitemap absolute settings
from taggit.managers import TaggableManager                                     #taggit for manage Tags

class Category(models.Model):
        name = models.CharField(max_length=255)
        def __str__(self):
            return self.name
        
class Post(models.Model):
    image =models.ImageField(upload_to='blog/',default='blog/default.jpg')
    author = models.ForeignKey(User, on_delete=models.CASCADE ,null=True)        #authorیک کلید فرعی واسطه به یوزر
    title = models.CharField(max_length=255)
    content = models.TextField()
    tags = TaggableManager()                                                     #taggit for manage Tags
    category = models.ManyToManyField(Category)
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    login_required = models.BooleanField(default=False)                          #login requirments in posts

    class Meta:
        ordering = ['created_date']
    def __str__(self):
        return self.title
    
    #sitemap absolute settings
    def get_absolute_url(self):
         return reverse('blog:single', kwargs={'pid': self.id})