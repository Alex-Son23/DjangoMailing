from django.contrib import admin

from models import Subscriber


@admin.register(Subscriber)
class AuthorAdmin(admin.ModelAdmin):
    pass
