from django.utils import timezone
from django.db import transaction
from django.shortcuts import get_object_or_404
from .models import GlobalDailyRoutine, Gym
from .ai import generar_rutina

def get_or_create_today_routine():
    today = timezone.localdate()
    
    routine, created = GlobalDailyRoutine.objects.get_or_create(date=today)

    if created or not routine.routines:
        try:
            nuevas_rutinas = generar_rutina()
            routine.routines = nuevas_rutinas
            routine.save()
        except Exception as e:
            print(f"Error en Gemini: {e}")
            
    return routine


def get_gym_by_uuid(uuid):
    return get_object_or_404(Gym, qr_token=uuid)
