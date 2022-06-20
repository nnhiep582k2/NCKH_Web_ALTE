from django.contrib import admin

from .models import contactEmail

from .models import FeedBack

# Register your models here.



class FeedBackAdmin(admin.ModelAdmin):
    list_display = ["Name","Email","Star","Number","WriteMessage"]
    search_fields = ['Name']
    list_filter = ["Name","Email","Star","Number","WriteMessage"]
admin.site.register(FeedBack,FeedBackAdmin)


class SendEmailAdmin(admin.ModelAdmin):
    list_display = ["id","Email"]
    search_fields =["id","Email"]
    list_filter = ["id","Email"]
admin.site.register(contactEmail,SendEmailAdmin)

