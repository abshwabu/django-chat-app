from django.urls import path
from chat import views


urlpatterns = [
    path('',views.lobby),
    path("<str:room_name>/", views.room, name="room"),
]