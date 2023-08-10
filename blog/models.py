from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
        name = models.CharField(max_length=255)
        def __str__(self):
            return self.name
class Post(models.Model):
    image =models.ImageField(upload_to='blog/',default='blog/default.jpg')
    #authorیک کلید فرعی وابسطغ به یوزر
    author = models.ForeignKey(User, on_delete=models.CASCADE ,null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    tags = models.CharField(max_length=255, blank=True, null=True)
    category = models.ManyToManyField(Category)
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_date']
    def __str__(self):
        return self.title
    
    