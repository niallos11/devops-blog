from django.contrib import admin
from .models import Contact
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Contact)
class AboutAdmin(SummernoteModelAdmin):

    list_display = ('title',)
    search_fields = ['title', 'content']
    summernote_fields = ('content',)
