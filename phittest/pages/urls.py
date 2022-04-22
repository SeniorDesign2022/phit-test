from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('',views.default_view, name='default'),
    path('dashboard/', views.CalendarView.as_view(), name='dashboard'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('survey/', views.survey_view, name='survey'),
    path('results/', views.ChartView.as_view(), name='results'),
    path('results/', views.results_view, name='results'),
    path('patients/', views.PatientsView.as_view(), name='patients'),
    path('patients/', views.patients_view, name='patients'),
    path('patients/<int:id>', views.IndividualPatientListView.as_view(), name='indivpatient'),
    path('patients/<int:id>', views.indiv_patients_view, name='indivpatient'),
   



]