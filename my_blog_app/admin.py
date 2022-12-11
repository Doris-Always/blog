from django.contrib import admin

# Register your models here.
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish', 'date_created','slug')
    list_filter = ('status','date_created',)
    raw_id_fields = ('author',)
    search_fields = ('title','body')
    prepopulated_fields = {'slug': ('title',)}
# admin.site.register(Post)
