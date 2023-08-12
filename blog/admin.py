from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}