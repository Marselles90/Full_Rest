from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Author


@receiver(post_save, sender=Author)
def create_author(created, **kwargs):
    if created:
        print('Author Создан')
    else:
        print('Author Изменен')
    return