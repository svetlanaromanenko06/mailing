from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView, UpdateView, DeleteView, CreateView

from blog.models import Blog
from mailing.forms import ClientForm, MessageForm, MailingForm
from mailing.models import Client, Mailing, Message, Log
import random

class ClientListView(LoginRequiredMixin, ListView):
    model = Client

    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)

class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mail:clients_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mail:clients_list')

class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('mail:clients_list')

class IndexView(TemplateView):
    """Класс отображения главной страницы сервиса"""

    template_name = 'mailing/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'

        # Получение количества рассылок всего
        total_mailings = Mailing.objects.count()
        context['total_mailings'] = total_mailings

        # Получение количества активных рассылок
        active_mailings = Mailing.objects.filter(is_active=True).count()
        context['active_mailings'] = active_mailings

        # Получение количества уникальных клиентов для рассылок
        total_clients = Client.objects.count()
        context['total_clients'] = total_clients


        # Получение всех статей блога
        all_blogs = list(Blog.objects.all())

        if len(all_blogs) >= 3:
            random_blogs = random.sample(all_blogs, 3)
        else:
            random_blogs = all_blogs

        context['random_blogs'] = random_blogs

        return context


class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.has_perm('mailing.can_manager_view'):
            return queryset
        return queryset.filter(owner=self.request.user)


class MailingCreateView(LoginRequiredMixin, CreateView):

    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['owner'] = self.request.user
        return kwargs

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class MailingDetailView(DetailView):
    model = Mailing


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['owner'] = self.request.user
        return kwargs

class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:messages_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class MessageListView(LoginRequiredMixin, ListView):
    model = Message

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.has_perm('mailing.can_manager_view'):
            return queryset
        return queryset.filter(owner=self.request.user)


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:messages_list')


class MessageDelete(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('mailing:messages_list')

class LogListView(LoginRequiredMixin, ListView):
    model = Log

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.has_perm('mailing.can_manager_view'):
            return queryset
        return queryset.filter(mailing__owner=self.request.user)