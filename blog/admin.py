from django.contrib import admin

from blog.models import Tag, Post


admin.site.register(Tag)
admin.site.register(Post)

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", "published_at", )}
    list_display = ('slug', 'published_at')