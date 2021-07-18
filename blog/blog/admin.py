from blog.views import post_detail
from django.contrib import admin
from .models import Post, comment

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug':('title',)}

@admin.register(comment)
class commentAdmin(admin.ModelAdmin):
    list_display = ('name', 'comment_text', 'post')


# admin.site.register(Post, PostAdmin)

