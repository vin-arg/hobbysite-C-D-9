from django.contrib import admin
from .models import PostCategory, Post

# Register your models here.
@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_on', 'updated_on')
    list_filter = ('category',)
    search_fields = ('title', 'entry')