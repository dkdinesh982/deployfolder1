from django.db import models
# from django.core.urlresolvers import reverse
from django.urls import reverse
# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=20)
    loc=models.CharField(max_length=30)
    sal=models.FloatField()
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})