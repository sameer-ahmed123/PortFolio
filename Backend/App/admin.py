from django.contrib import admin
from App.models import *

class ContactAdmin(admin.ModelAdmin):
    model = Contact
    list_display = ["name", "subject", "email"]


# Register your models here.
admin.site.register(Project)
admin.site.register(Contact,ContactAdmin)