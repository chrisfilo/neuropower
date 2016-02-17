from __future__ import unicode_literals
from django.db import models

class NiftiModel(models.Model):
    url = models.URLField()
    location = models.CharField(max_length=300,default="/Users/Joke/Documents/Onderzoek/neuropower/neuropower-dev/neuropower/static_in_pro/our_static/img/zstat1.nii.gz")
    def __unicode__(self): # Python 3: __str__
        return self

class ParameterModel(models.Model):
    ZorT_c = ((1,"Z"),(2,"T"))
    ExcUnits_c = ((1,"units = p-values (SPM default)"),(2,"units = t-values (FSL default)"))
    Samples_c = ((1, ("One-sample")),(2, ("Two-sample")))
    ZorT = models.IntegerField(choices=ZorT_c)
    ExcUnits = models.IntegerField(choices=ExcUnits_c)
    Exc = models.DecimalField(max_digits=5,decimal_places=2)
    Subj = models.IntegerField()
    Samples = models.IntegerField(choices=Samples_c)
    Smoothx = models.DecimalField(max_digits=5,decimal_places=2)
    Smoothy = models.DecimalField(max_digits=5,decimal_places=2)
    Smoothz = models.DecimalField(max_digits=5,decimal_places=2)
    Voxx = models.DecimalField(max_digits=5,decimal_places=2)
    Voxy = models.DecimalField(max_digits=5,decimal_places=2)
    Voxz = models.DecimalField(max_digits=5,decimal_places=2)
    def __unicode__(self): # Python 3: __str__
        return self
