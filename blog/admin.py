from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'creation_date', 'views_count')
    list_filter = ('creation_date', 'views_count')
    ordering = ('creation_date',)
