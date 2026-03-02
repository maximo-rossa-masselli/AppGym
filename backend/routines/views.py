import time
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .services import get_or_create_today_routine, get_gym_by_uuid
from .serializers import GlobalDailyRoutineSerializer

@api_view(["GET"])
def today_routine_view(req):
    start = time.time()
    print(">>> DEBUG: Entrando a today_routine_view")
    routine = get_or_create_today_routine()
    serializer = GlobalDailyRoutineSerializer(routine)
    print(f"<<< DEBUG: today_routine_view finalizada en {time.time() - start:.2f}s")
    return Response(serializer.data)

@api_view(['GET'])
def selected_gym_view(req, qr_token):
    start = time.time()
    print(f">>> DEBUG: Entrando a selected_gym_view | Token: {qr_token}")
    gym = get_gym_by_uuid(qr_token)
    routine = get_or_create_today_routine()
    
    resp = Response({
        "gym": {
            "name": gym.name,
            "logo": gym.logo,
            "primary_color":gym.primary_color,
            "secondary_color":gym.secondary_color
        },
        "rutinas_disponibles": list(routine.routines.keys())
    })
    print(f"<<< DEBUG: selected_gym_view finalizada en {time.time() - start:.2f}s")
    return resp

@api_view(["GET"])
def selected_routine_view(req, qr_token, type):
    start = time.time()
    print(f">>> DEBUG: Entrando a selected_routine_view | Token: {qr_token} | Tipo: {type}")
    gym = get_gym_by_uuid(qr_token)
    routine = get_or_create_today_routine()

    if type not in routine.routines:
        print(f"DEBUG: [!] Tipo '{type}' no encontrado en la rutina actual.")
        return Response(
            {"detail": "Tipo de rutina no encontrado"},
            status=status.HTTP_404_NOT_FOUND)

    selected_routine = routine.routines[type]
    
    resp = Response({
        "gym": {
            "name":gym.name,
            "logo":gym.logo,
            "primary_color":gym.primary_color,
            "secondary_color":gym.secondary_color
        },
        "type":type,
        "routine":selected_routine
    })
    print(f"<<< DEBUG: selected_routine_view finalizada en {time.time() - start:.2f}s")
    return resp