from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from .models import Survey
from django.contrib.auth.models import User
from .forms import SurveyForm

# Create your views here.

@login_required(login_url='/login/')
def dashboard(request):
    return redirect('pages:dashboard')

@login_required(login_url='/login/')
def survey_view(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            print("user: ", request.user)
            all_entries = Survey.objects.all()
            user_entries = []
            for entry in all_entries:
                if entry.user == request.user:
                    user_entries.append(entry)
            print(len(user_entries))
            if len(user_entries) is not 0:
                last_entry_date = user_entries[len(user_entries)-1].date
                last_entry_id = user_entries[len(user_entries)-1].survey_id
            
                print(last_entry_id)
                form.save()
                if last_entry_date == Survey.objects.latest('date').date:
                    Survey.objects.filter(survey_id=last_entry_id).delete()
            form.save()
            return redirect('pages:survey')
    else:
        form = SurveyForm()
    return render(request, 'pages/survey.html', {'form': form})


@login_required(login_url='/login/')
def results_view(request):
    return redirect('pages:results')


@login_required(login_url='/login/')
def patients_view(request):
    return redirect('pages:patients')


@login_required(login_url='/login/')
def indiv_patients_view(request, id):
    return redirect('pages:indivpatient')


@login_required(login_url='/login/')
def calendar_data(request):
    mylist = [10,22,33,45]
    return render(request, 'pages/dashboard.html', {'demolist': mylist})

class ChartView(TemplateView):
    template_name = 'pages/results.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Survey.objects.all().order_by('date')
        return context

class PatientsView(TemplateView):
    template_name = 'pages/patients.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = User.objects.filter(is_staff=False)
        return context

class CalendarView(TemplateView):
    template_name = 'pages/dashboard.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Survey.objects.all().order_by('date')
        return context


class IndividualPatientListView(TemplateView):
    template_name = 'pages/indiv_patients.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs2"] = User.objects.filter(is_staff=False)
        context["qs"] = Survey.objects.all().order_by('date')
        return context