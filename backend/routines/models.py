from django.db import models
from django.core.validators import RegexValidator
import uuid

# Create your models here.
class Gym(models.Model):
    name = models.CharField(max_length=100)
    qr_token = models.UUIDField(
        default =uuid.uuid4,
        unique=True,
        editable=False
    )
    logo = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    hex_color_validator = RegexValidator(
        regex=r'^#(?:[0-9a-fA-F]{3}){1,2}$',
        message='Ingresa un color hexadecimal válido (ej: #FF5733)'
    )
    
    primary_color = models.CharField(
        max_length=7,
        validators=[hex_color_validator],
        default='#000000'
    )
    secondary_color = models.CharField(
        max_length=7,
        validators=[hex_color_validator],
        default='#FFFFFF'
    )

    def __str__(self):
        return self.name
    

class GlobalDailyRoutine(models.Model):
    date = models.DateField(unique=True)
    routines = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rutina del día {self.date}"