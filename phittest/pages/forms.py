from django import forms
from .models import Survey
from pages import models
from django.forms.widgets import RadioSelect
from django.utils.translation import gettext_lazy as _


# class SurveyChoices(models.TextChoices):
#     NAA = 0, _('Not at all')
#     ONE = 1, _('Less than 1 time in 5')
#     TWO = 2, _('Less than half the time')
#     THREE = 3, _('About half the time')
#     FOUR = 4, _('More than half the time')
#     FIVE = 5, _('Almost always')

class SurveyForm(forms.ModelForm):
    """Contains definition for the survey."""
    class Meta:
        """Metadata options for this form."""
        model = Survey
        exclude = ['user', 'total_score']
        widgets = {
            'incomplete_emptying': RadioSelect(choices=models.Survey.NUMCHOICES),
            'frequency': RadioSelect(choices=models.Survey.NUMCHOICES),
            'intermittency': RadioSelect(choices=models.Survey.NUMCHOICES),
            'urgency': RadioSelect(choices=models.Survey.NUMCHOICES),
            'weak_stream': RadioSelect(choices=models.Survey.NUMCHOICES),
            'straining': RadioSelect(choices=models.Survey.NUMCHOICES),
            'nocturia': RadioSelect(choices=models.Survey.NUMCHOICES),
            'quality_of_life': RadioSelect(choices=models.Survey.QOLCHOICES),
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


