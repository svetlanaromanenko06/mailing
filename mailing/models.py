from django.utils import timezone

from django.conf import settings
from django.db import models

NULLABLE = {'null': True, 'blank': True }


class Client(models.Model):
    email = models.EmailField(unique=True, verbose_name='email')
    fullname = models.CharField(max_length=100, verbose_name='полное имя')
    comment = models.TextField(max_length=250, verbose_name='комментарий', **NULLABLE)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='владелец')

    def __str__(self):
        return f'{self.fullname} - {self.email}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'
        ordering = ['email']


class Message(models.Model):
    message_subject = models.CharField(max_length=100, verbose_name='тема письма')
    message = models.TextField(verbose_name='cообщение')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='владелец сообщения',**NULLABLE)


    def __str__(self):
        return f'{self.message_subject}: {self.message}'

    class Meta:
        verbose_name = "сообщение"
        verbose_name_plural = "сообщения"


class Mailing(models.Model):

    frequency_choices = [
        ('daily', 'ежедневно'),
        ('weekly', 'еженедельно'),
        ('monthly', 'ежемесячно')
    ]

    status_choices = [
        ("created", "Создана"),
        ("completed", "Завершена"),
        ("started", "Запущена"),
    ]


    start_time = models.DateTimeField(default=timezone.now, verbose_name='время начала рассылки')
    end_time = models.DateTimeField(**NULLABLE, verbose_name='время окончания рассылки')
    frequency = models.CharField(max_length=50, choices=frequency_choices, verbose_name='периодичность')
    status = models.CharField(max_length=50, choices=status_choices, verbose_name='статус')
    clients = models.ManyToManyField(Client, verbose_name='клиенты')
    is_active = models.BooleanField(default=True, verbose_name='статус активности')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='content')
    last_sent = models.DateTimeField(**NULLABLE, verbose_name='последняя отправка')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='владелец рассылки')



    def __str__(self):
        return f'{self.start_time} , {self.frequency} , {self.status}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'



class Log(models.Model):

    STATUS_CHOICE = (
        ("success", "Успешно"),
        ("failed", "Неуспешно"),
    )
    mailing = models.ForeignKey(Mailing, verbose_name='рассылка', on_delete=models.CASCADE)
    last_attempt = models.DateTimeField(verbose_name='время последней попытки')
    status = models.CharField(max_length=7, choices=STATUS_CHOICE, verbose_name='статус попытки')
    message = models.CharField(max_length=200, verbose_name='сообщение', **NULLABLE)

    def __str__(self):
        return f'{self.mailing} ({self.last_attempt}) - {self.status}'

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'