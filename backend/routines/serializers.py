from rest_framework import serializers
from .models import GlobalDailyRoutine, Gym

class GlobalDailyRoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalDailyRoutine
        fields = ['date', 'routines', 'created_at']
