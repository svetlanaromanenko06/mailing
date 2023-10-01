from datetime import datetime, timezone
from django.core.mail import send_mail
from mailing.models import Mailing, Log, Client
from django.conf import settings



def get_objects_for_send(Mailing):
    '''Возвращает список рассылок для отправки'''

    now = timezone.now()
    objects_list = []

    for mailing in Mailing.objects.all():

        is_daily_valid = not mailing.last_sent or mailing.last_sent <= now - datetime.timedelta(days=1)
        is_weekly_valid = not mailing.last_sent or mailing.last_sent <= now - datetime.timedelta(days=7)
        is_monthly_valid = not mailing.last_sent or mailing.last_sent <= now - datetime.timedelta(days=30)

        if all([mailing.status in ['created', 'completed'],
            mailing.start_time.time() < now.time(),
            mailing.start_time < now,
            now < mailing.completion_time]
               ):
            if  all([mailing.frequency == 'daily', is_daily_valid]):
                objects_list.append(mailing)
                
            elif  all([mailing.frequency == 'weekly', is_weekly_valid]):
                objects_list.append(mailing)
                
            elif  all([mailing.frequency == 'monthly', is_monthly_valid]):
                objects_list.append(mailing)
     

    return objects_list



def send_mailing():
    try:
        mailing_list = Mailing.objects.all().get_objects_for_send()
        for mailing in mailing_list:


            if mailing.is_active and mailing.status == "created":

                recipient_list = []
                clients = Client.objects.all().filter(owner=mailing.owner)
                for client in clients:
                    recipient_list.append(client.client_email)


                for recipient in recipient_list:

                    subject = mailing.message.message_subject
                    text = mailing.message.message

                    from_email = settings.EMAIL_HOST_USER


                    send_mail(subject, text, from_email, [recipient])


                    Log.objects.create(
                        mailing=mailing,
                        last_attempt=datetime.datetime.now(),
                        status="success",
                        message="Отправлено успешно"
                    )


                mailing.status = "completed"
                mailing.last_sent = datetime.datetime.now()
                mailing.save()
            else:

                Log.objects.create(
                    mailing=mailing,
                    last_attempt=datetime.datetime.now(),
                    status="failed",
                    message="Рассылка не активна или уже отправлена"
                )
    except Mailing.DoesNotExist:
        pass








