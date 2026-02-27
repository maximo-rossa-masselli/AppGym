from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .services import get_or_create_today_routine, get_gym_by_uuid
from .serializers import GlobalDailyRoutineSerializer

# Create your views here.
@api_view(["GET"])
def today_routine_view(req):
    routine = get_or_create_today_routine()
    serializer = GlobalDailyRoutineSerializer(routine)
    return Response(serializer.data)

@api_view(['GET'])
def selected_gym_view(req, qr_token):
    gym = get_gym_by_uuid(qr_token)
    routine = get_or_create_today_routine()
    
    return Response({
        "gym": {
            "name": gym.name,
            "logo": gym.logo,
            "primary_color":gym.primary_color,
            "secondary_color":gym.secondary_color
        },
        "rutinas_disponibles": list(routine.routines.keys())
    })

@api_view(["GET"])
def selected_routine_view(req, qr_token, type):
    gym = get_gym_by_uuid(qr_token)
    routine = get_or_create_today_routine()

    if type not in routine.routines:
        return Response(
            {"detail": "Tipo de rutina no encontrado"},
            status=status.HTTP_404_NOT_FOUND)

    selected_routine = routine.routines[type]
    
    return Response({
        "gym": {
            "name":gym.name,
            "logo":gym.logo,
            "primary_color":gym.primary_color,
            "secondary_color":gym.secondary_color
        },
        "type":type,
        "routine":selected_routine
    })