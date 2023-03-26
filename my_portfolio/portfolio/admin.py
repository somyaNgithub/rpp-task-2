from django.contrib import admin
from portfolio.models import visitor_note


class VisitorAdmin(admin.ModelAdmin):
    list_display = ('full_name','email','mob_number','email_subject','message')


# Register your models here.
admin.site.register(visitor_note,VisitorAdmin)
