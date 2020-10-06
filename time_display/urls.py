from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('time_display', views.redir),
    path('bonus', views.bonus)#BONUS: Come up with a different way to retrieve the datetime
]