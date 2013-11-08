from django.db import models
from django.forms import ModelForm
# Create your models here.

class Thermostat(models.Model):
    hold_temp = models.IntegerField() 
    temp_range = models.IntegerField()

class TemperatureReading(models.Model):
    temperature = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)


#------------------------------Model Forms------------------------------#

class TemperatureReadingForm(ModelForm):
    class Meta:
        model = TemperatureReading

