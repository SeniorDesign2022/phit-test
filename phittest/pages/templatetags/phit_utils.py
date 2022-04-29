"""Provides helpful utility tags to be used in Django tamplete."""
from django.template.defaulttags import register as tag_register
from django import template
import os

register = template.Library()
@tag_register.filter(name='is_doctor')
def is_doctor(user):
    """Checks if the user is a trial coordinator.

    Args:
        user (django.contrib.auth.models.User): the user to check group.

    Returns:
        bool: True is the user is a trial coordinator.
    """
    return user.groups.filter(name='doctor').exists()