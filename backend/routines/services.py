import time
from django.http import Http404
from django.utils import timezone
from .models import GlobalDailyRoutine, Gym
from .ai import generar_rutina, rutina_fallback

def get_or_create_today_routine():
    start_time = time.time()
    today = timezone.localdate()
    print(f"--- DEBUG [{today}]: Iniciando consulta de rutina ---")
    
    # 1. Intentamos traer la rutina de la DB
    routine, created = GlobalDailyRoutine.objects.get_or_create(date=today)
    
    # 2. Si es nueva o está vacía, intentamos llenar con Gemini
    if created or not routine.routines:
        print("DEBUG: [!] La rutina está vacía. Solicitando a Gemini...")
        try:
            # Llamamos a la IA (que ya tiene sus propios reintentos internos)
            nuevas_rutinas = generar_rutina()
            
            # Si llegamos acá, Gemini respondió bien: GUARDAMOS.
            routine.routines = nuevas_rutinas
            routine.save()
            print(f"DEBUG: Rutina IA guardada exitosamente en {time.time() - start_time:.2f}s.")
        
        except Exception as e:
            # Si Gemini falló 3 veces, usamos fallback pero NO guardamos en DB
            print(f"ALERTA: Gemini falló tras reintentos. Usando fallback temporal. Error: {e}")
            routine.routines = rutina_fallback()
            # IMPORTANTE: No hacemos routine.save() aquí para permitir reintentos futuros
    else:
        print("DEBUG: Rutina encontrada en caché de DB. Saltando llamada a IA.")
            
    print(f"--- DEBUG: Proceso finalizado en {time.time() - start_time:.2f}s ---")
    return routine

def get_gym_by_uuid(uuid):
    try:
        print(f"DEBUG: Buscando gimnasio con UUID: {uuid}")
        return Gym.objects.get(qr_token=uuid)
    except Gym.DoesNotExist:
        print(f"ERROR: El gimnasio con UUID {uuid} NO EXISTE.")
        raise Http404("Gimnasio no encontrado")
    except Exception as e:
        print(f"ERROR CRÍTICO: {e}")
        raise e