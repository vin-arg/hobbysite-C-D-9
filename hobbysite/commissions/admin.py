from django.contrib import admin
from .models import Commission, Comment

class CommissionAdmin(admin.ModelAdmin):
    model = Commission
    list_display = ('title', 'description', 'people_required', 'created_on',)
    list_filter = ('title',)
    search_fields = ('title',)


class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ('commission', 'created_on', 'updated_on',)
    search_fields = ('commission', 'title', 'entry',)

admin.site.register(Commission, CommissionAdmin)
admin.site.register(Comment, CommentAdmin)