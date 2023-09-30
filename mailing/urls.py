from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import ClientListView, ClientCreateView, ClientDetailView, ClientUpdateView, ClientDeleteView, \
    IndexView, MailingListView, MessageListView, MessageCreateView, MessageDetailView, MessageUpdateView, MessageDelete, \
    MailingCreateView, MailingDetailView, MailingUpdateView, LogListView

app_name = MailingConfig.name


class MailingDeleteView:
    pass


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('mailing/', MailingListView.as_view(), name='mailing_list'),
    path('mailing/create/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailing/<int:pk>/', MailingDetailView.as_view(), name='mailing_view'),
    path('mailing/<int:pk>/update/', MailingUpdateView.as_view(), name='mailing_update'),
    path('client/', ClientListView.as_view(), name='client_list'),
    path('client/create/', ClientCreateView.as_view(), name='client_create'),
    path('client/<int:pk>/', ClientDetailView.as_view(), name='client_view'),
    path('client/<int:pk>/update/', ClientUpdateView.as_view(), name='client_update'),
    path('client/<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),
    path('messages/', MessageListView.as_view(), name='message_list'),
    path('messages/create/', MessageCreateView.as_view(), name='message_create'),
    path('messages/<int:pk>/', MessageDetailView.as_view(), name='message_view'),
    path('messages/<int:pk>/update/', MessageUpdateView.as_view(), name='message_update'),
    path('messages/<int:pk>/delete/', MessageDelete.as_view(), name='message_delete'),
    path('log/log_list/', LogListView.as_view(), name='log_list'),
]
