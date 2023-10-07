from django.urls import path
from . import views


urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("personal1", views.curdp, name="personal1"),
    path("horarios", views.horarios, name="horarios"),
    path("buses", views.buses1, name="buses"),
    path("calendario", views.calendario, name="calendario"),
    path("horarios", views.curdp, name="horarios"),
]
