from __future__ import unicode_literals
from django.contrib import admin
from models import Block
# Register your models here


class BlockAdmin(admin.ModelAdmin):
    list_display = ("name", "desc", "manager", "create_timestamp", "last_update_timestamp")

admin.site.register(Block, BlockAdmin)
