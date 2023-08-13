from django.contrib import admin
from .models import Tutorials
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Tutorials)
class TutorialsAdmin(SummernoteModelAdmin):

    list_display = ('title',)
    search_fields = ['title', 'content']
    summernote_fields = ('content',)
