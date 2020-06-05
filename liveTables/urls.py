from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('past', views.past, name='past'),
    path('live', views.live, name='live'),
    path('scheduled', views.schedule, name='schedule')
]