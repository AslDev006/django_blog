from django.contrib import admin
from .models import *


@admin.register(Post_Model)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'publish_time']
    list_filter = ['publish_time']
    prepopulated_fields = {'slug': ['title']}
    date_hierarchy = 'publish_time'
    search_fields = ['title', 'body']
    ordering = ['publish_time', 'status']


@admin.register(Comment_models)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'message', 'active']
    list_filter = [ 'active']
    search_fields = ['body']
    actions = ['disable_comments', 'activate_comments']
    def disable_comments(self, request, queryset):
        queryset.update(active=False)
    def activate_comments(self, request, queryset):
        queryset.update(active=True)