from django.contrib import admin

# Register your models here.

from configuration.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'domain_url']
