from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
    path('christmas', views.christmas, name='christmas'),
    path('tiradentes', views.tiradentes, name='tiradentes'),
]
