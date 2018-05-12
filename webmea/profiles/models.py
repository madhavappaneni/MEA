from __future__ import unicode_literals
from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
CHOICES = (
    ('ME-II', 'ME-II'),
    ('ME-III', 'ME-III'),
    ('ME-IV', 'ME-IV'),
    ('PE-II', 'PE-II'),
    ('PE-III', 'PE-III'),
    ('PE-IV', 'PE-IVI'),
)
def validate(value):
    if len(value)!=10:
        raise ValidationError(
            _('%(value)s is not an 10 digit number'),
            params={'value': value},
        )
class ProfileModel(models.Model):
    name = models.CharField(max_length=40, blank=True, null=True, verbose_name="Name")
    bra = models.CharField(max_length=10, choices=CHOICES, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=10, validators=[validate])
    def __unicode__(self):
        return self.name


