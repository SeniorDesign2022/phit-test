from django import forms
from .models import Survey
from pages import models
from django.forms.widgets import RadioSelect, DateInput
from django.utils.translation import gettext_lazy as _


class SurveyForm(forms.ModelForm):
    """Contains definition for the survey."""
    class Meta:
        """Metadata options for this form."""
        model = Survey
        exclude = ['survey_id', 'user', 'total_score']
        widgets = {
            'date': DateInput(attrs={'class': 'datepicker'}),
            'incomplete_emptying': RadioSelect(choices=models.Survey.NUMCHOICES),
            'frequency': RadioSelect(choices=models.Survey.NUMCHOICES,attrs={'class' : 'radiobtn'}),
            'intermittency': RadioSelect(choices=models.Survey.NUMCHOICES),
            'urgency': RadioSelect(choices=models.Survey.NUMCHOICES),
            'weak_stream': RadioSelect(choices=models.Survey.NUMCHOICES),
            'straining': RadioSelect(choices=models.Survey.NUMCHOICES),
            'nocturia': RadioSelect(choices=models.Survey.NUMCHOICES),
            'quality_of_life': RadioSelect(choices=models.Survey.QOLCHOICES),
    
        }
        help_texts = {
            'incomplete_emptying': '*It does not feel like I empty my bladder all the way',
        }

    #     labels = {
    #         # 'termination_date': 'Date of Termination From Study',
    #         # 'termination_reason_field': '1. Reason for Termination (check one)',
    #         # 'termination_reason_comment_field': 'Specify other reason:',
    #         # 'comment_field': '2. Comments'
    #     }
    #     widgets = {
    #         # 'termination_date_field': DateInput(attrs={'class': 'datepicker'}),
    #         # 'termination_reason_field': RadioSelect(
    #         #     choices=EndOfStudyForm.TerminationReason.choices),
    #         # 'comment_field': Textarea(attrs={'rows': 2})
    #     }
        # fields = ['incomplete_emptying', 'frequency', 'intermittency', 'urgency', 'weak_stream', 'straining', 'nocturia', 'quality_of_life', 'total_score']


