from django.urls import path
from .views import today_routine_view, selected_gym_view, selected_routine_view

urlpatterns = [
    path("routine/today/", today_routine_view),
    path('public/<uuid:qr_token>/', selected_gym_view),
    path("public/<uuid:qr_token>/routine/<str:type>/", selected_routine_view)
]