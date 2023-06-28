from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Student
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER


@receiver(post_save, sender=Student)
def send_student_notification(sender, instance, created, **kwargs):
    if created:
        subject = f'Добро пожаловать в школу {instance.class_name.school}'
        message = f'Дорогой {instance.full_name},\n\nДобро пожаловать в нашу школу {instance.class_name.school}!'
        message += f'Вы были добавлены в класс {instance.class_name.name} под руководством учителя {instance.class_name.teacher}.'
        from_email = EMAIL_HOST_USER
        to_email = instance.email
        send_mail(subject, message, from_email, [to_email])
