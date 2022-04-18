from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from .models import Survey



from .forms import SurveyForm

# Create your views here.

@login_required
def dashboard(request):

    return render(request, 'pages/dashboard.html')

@login_required
def survey_view(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('pages:survey')
    else:
        form = SurveyForm()
        
    return render(request, 'pages/survey.html', {'form': form})

@login_required
def results_view(request):
    return render(request, 'pages/results.html')


@login_required
def patients_view(request):
    return render(request, 'pages/patients.html')


class ChartView(TemplateView):
    template_name = 'pages/results.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Survey.objects.all()
        return context