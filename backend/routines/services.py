from django.utils import timezone
from django.db import transaction
from django.shortcuts import get_object_or_404
from .models import GlobalDailyRoutine, Gym
from .ai import generar_rutina

def get_or_create_today_routine():
    today = timezone.localdate()

    with transaction.atomic():
        routine, created = GlobalDailyRoutine.objects.get_or_create(date=today)
        
        if created:
            routine.routines = generar_rutina()
            routine.save()

    return routine


def get_gym_by_uuid(uuid):
    return get_object_or_404(Gym, qr_token=uuid)
