from django.contrib import admin
from .models import AskLetter


@admin.register(AskLetter)
class AskLetterAdmin(admin.ModelAdmin):
    list_display = ["name", "mail", "is_read"]
