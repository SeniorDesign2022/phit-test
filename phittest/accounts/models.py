from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

# class surveyChoices(models.TextChoices):
#     """Enumeration for the Demographics/Medical History Form."""
#     NAA = 0, _('Not at all')
#     ONE = 1, _('Less than 1 time in 5')
#     TWO = 2, _('Less than half the time')
#     THREE = 3, _('About half the time')
#     FOUR = 4, _('More than half the time')
#     FIVE = 5, _('Almost always')


# class Survey(models.Model):
#     """Model for the survey questions."""
#     incomplete_emptying = models.IntegerField(blank=False, null=True)
#     frequency = models.IntegerField(blank=False, null=True)
#     intermittency = models.IntegerField(blank=False, null=True)
#     urgency = models.IntegerField(blank=False, null=True)
#     weak_stream = models.IntegerField(blank=False, null=True)
#     straining = models.IntegerField(blank=False, null=True)
#     nocturia = models.IntegerField(blank=False, null=True)
#     quality_of_life = models.IntegerField(blank=False, null=True)
#     total_score = models.IntegerField(blank=True, null=True)

#     # def __init__(self, *args, **kwargs):
#     #     """Automatically fills the 'total_score' field."""

