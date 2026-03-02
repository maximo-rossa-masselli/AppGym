import time
from django.utils import timezone
from django.db import transaction
from django.shortcuts import get_object_or_404
from .models import GlobalDailyRoutine, Gym
from .ai import generar_rutina

def get_or_create_today_routine():
    start_time = time.time()
    today = timezone.localdate()
    print(f"--- DEBUG [{today}]: Iniciando get_or_create_today_routine ---")
    
    # Intentamos traer la rutina de la base de datos
    routine, created = GlobalDailyRoutine.objects.get_or_create(date=today)
    print(f"DEBUG: Routine en DB. ¿Se creó una nueva fila?: {created}")

    # Si se acaba de crear o el campo JSON está vacío, llamamos a la IA
    if created or not routine.routines:
        print("DEBUG: [!] La rutina está vacía o es nueva. LLAMANDO A GEMINI...")
        ai_start = time.time()
        try:
            nuevas_rutinas = generar_rutina()
            print(f"DEBUG: Gemini respondió exitosamente en {time.time() - ai_start:.2f} segundos.")
            routine.routines = nuevas_rutinas
            routine.save()
            print("DEBUG: Rutina guardada en Supabase correctamente.")
        except Exception as e:
            print(f"ERROR CRÍTICO en Gemini tras {time.time() - ai_start:.2f}s: {e}")
    else:
        print("DEBUG: Rutina encontrada en DB con datos. Saltando llamada a IA para ahorrar tiempo.")
            
    print(f"--- DEBUG: get_or_create_today_routine finalizado en {time.time() - start_time:.2f}s ---")
    return routine

def get_gym_by_uuid(uuid):
    print(f"DEBUG: Buscando gimnasio con UUID: {uuid}")
    return get_object_or_404(Gym, qr_token=uuid)