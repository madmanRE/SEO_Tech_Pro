from django.contrib import admin
from .models import BlogPost, BlogCategory


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "slug",
        "image",
        "created_at",
        "views",
        "is_active",
    ]
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ["created_at"]
    search_fields = ["title", "slug"]


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "count_items"]
    prepopulated_fields = {"slug": ("title",)}

    def count_items(self, cat):
        return cat.count_items()

    count_items.short_description = "Статей в категории"
