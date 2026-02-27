from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Gym
from .utils import generar_qr_para_gym


@receiver(post_save, sender=Gym)
def crear_qr_al_crear_gym(sender, instance, created, **kwargs):
    if created and not instance.qr_image:
        generar_qr_para_gym(instance)
        instance.save()