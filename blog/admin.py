from django.contrib import admin
from django.contrib import admin
from .models import Post 
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('title','status','created_date','id')
    list_filter = ('published_date',)
    search_fields = ('title','content')



admin.site.register(Post,PostAdmin)