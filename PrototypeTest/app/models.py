"""
Definition of models.
"""

from django.db import models

# Create your models here.
GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)

COLOR_CHOICES = (
    ('green','GREEN'),
    ('blue', 'BLUE'),
    ('red','RED'),
    ('orange','ORANGE'),
    ('black','BLACK'),
)

class MyModel(models.Model):
  color = models.CharField(max_length=6,choices=COLOR_CHOICES,
                 default='green')