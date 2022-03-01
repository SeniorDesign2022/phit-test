from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
]