from django.contrib import admin
from .models import Post ,Category
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('title','author','status','created_date','id')
    list_filter = ('published_date',)
    search_fields = ('title','content','author')


admin.site.register(Category)
admin.site.register(Post,PostAdmin)