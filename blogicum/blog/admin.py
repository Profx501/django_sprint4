from django.contrib import admin
from .models import Category, Location, Post

admin.site.empty_value_display = 'Не задано'
admin.site.register(Category)
admin.site.register(Location)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'pub_date',
        'author',
        'category',
        'is_published'
    )

    list_editable = (
        'is_published',
        'category'
    )

    list_per_page = 10
    search_fields = ('title',)
    list_filter = ('author', 'category', 'created_at')
    ordering = ('title',)
