from django.db import models
from django.contrib.auth.models import User

from django.utils.translation import gettext_lazy as _

# Create your models here.

class Survey(models.Model):
    """Model for the survey questions."""
    
    NUMCHOICES = (
        (0, 'Not at all'),
        (1, 'Less than 1 time in 5'),
        (2, 'Less than half the time'),
        (3, 'About half the time'),
        (4, 'More than half the time'),
        (5, 'Almost always'),
    )

    QOLCHOICES = (
        (0, 'Terrible'),
        (1, 'Unhappy'),
        (2, 'Mostly dissatisfied'),
        (3, 'Mixed: about equally satisfied and dissatisfied'),
        (4, 'Mostly satisfied'),
        (5, 'Pleased'),
        (6, 'Delighted'),
    )
    survey_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    date = models.DateField(null=True,auto_now_add=True) #auto_now_add=True
    incomplete_emptying = models.IntegerField(blank=False, null=True, default=0)
    frequency = models.IntegerField(blank=False, null=True, default=0)
    intermittency = models.IntegerField(blank=False, null=True, default=0)
    urgency = models.IntegerField(blank=False, null=True, default=0)
    weak_stream = models.IntegerField(blank=False, null=True, default=0)
    straining = models.IntegerField(blank=False, null=True, default=0)
    nocturia = models.IntegerField(blank=False, null=True, default=0)
    quality_of_life = models.IntegerField(blank=False, null=True, default=0)
    total_score = models.IntegerField(blank=True, null=True, default=0)
    event_change = models.TextField(blank=True, null=True)

    def save(self):
        self.total_score = self.incomplete_emptying + self.frequency + self.intermittency + self.urgency + self.weak_stream + self.straining + self.nocturia
        super(Survey, self).save()

    def __str__(self) -> str:
        """Returns string-formatted objects."""
        return f'Survey responses for ' + User.get_full_name(self.user) + ' on ' + str(self.date) + ' (' + str(self.survey_id) + ')'
    # class surveyChoices(models.TextChoices):
    #     """Enumeration for the Demographics/Medical History Form."""
    #     NAA = 0, _('Not at all')
    #     ONE = 1, _('Less than 1 time in 5')
    #     TWO = 2, _('Less than half the time')
    #     THREE = 3, _('About half the time')
    #     FOUR = 4, _('More than half the time')
    #     FIVE = 5, _('Almost always')
    # def __init__(self, *args, **kwargs):
    #     """Automatically fills the 'total_score' field."""

