from django.contrib import admin

from .models import IndexSendEmail


class SendEmailAdmin(admin.ModelAdmin):
    list_display = ["id","Email"]
    search_fields =["id","Email"]
    list_filter = ["id","Email"]
admin.site.register(IndexSendEmail,SendEmailAdmin)
