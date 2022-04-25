from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from .models import Survey
from django.contrib.auth.models import User
from .forms import SurveyForm

# Create your views here.

def default_view(request):
    return(redirect('login'))

@cache_control(no_cache=True, must_revalidate=True)    
@login_required(login_url='/login/')
def dashboard(request):
    print("hello")
    print(request.user)
    if request.user.is_authenticated():  
        return redirect('pages:dashboard')
    else:
        return (redirect('login'))

@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url='/login/')
def survey_view(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            all_entries = Survey.objects.all()
            user_entries = []
            for entry in all_entries:
                if entry.user == request.user:
                    user_entries.append(entry)
            if len(user_entries) != 0:
                last_entry_date = user_entries[len(user_entries)-1].date
                last_entry_id = user_entries[len(user_entries)-1].survey_id
                form.save()
                if last_entry_date == form.instance.date:
                    Survey.objects.filter(survey_id=last_entry_id).delete()
            form.save()
            return redirect('pages:survey')
    else:
        form = SurveyForm()
    return render(request, 'pages/survey.html', {'form': form})

@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url='/login/')
def results_view(request):
    if request.user.is_authenticated():  
        return redirect('pages:results')
    else:
        return (redirect('login'))

@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url='/login/')
def patients_view(request):
    if request.user.is_authenticated():  
        return redirect('pages:patients')
    else:
        return (redirect('login'))

@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url='/login/')
def indiv_patients_view(request, id):
    if request.user.is_authenticated():  
        return redirect('pages:indivpatient')
    else:
        return (redirect('login'))

@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url='/login/')
def calendar_data(request):
    if request.user.is_authenticated():  
        mylist = [10,22,33,45]
        return render(request, 'pages/dashboard.html', {'demolist': mylist})
    else:
        return (redirect('login'))
    

class ChartView(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'
    template_name = 'pages/results.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Survey.objects.all().order_by('date')
        return context

class PatientsView(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'
    template_name = 'pages/patients.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = User.objects.filter(is_staff=False)
        context["datas"] = Survey.objects.all().order_by('date')
        return context

class CalendarView(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'
    template_name = 'pages/dashboard.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Survey.objects.all().order_by('date')
        return context


class IndividualPatientListView(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'login'
    template_name = 'pages/indiv_patients.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs2"] = User.objects.filter(is_staff=False)
        context["qs"] = Survey.objects.all().order_by('date')
        return context