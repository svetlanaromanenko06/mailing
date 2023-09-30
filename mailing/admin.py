from django.contrib import admin
from mailing.models import Client, Mailing, Message


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email', 'fullname',)



@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'start_time', 'end_time', 'frequency', 'status', 'message')
    list_filter = ('status', 'frequency')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('message_subject', 'message')