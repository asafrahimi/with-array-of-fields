from djongo import models
from django.db import models
from django import forms
#from django.contrib.postgres.fields import ArrayField
#from djangotoolbox.fields import ListField, EmbeddedModelField
#from django_better_admin_arrayfield.models.fields import ArrayField
#from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
#from django_postgres_extensions.models.fields import ArrayField
from django_postgres_extensions.models.fields import HStoreField, JSONField, ArrayField
from django.contrib.postgres.operations import HStoreExtension
from django_postgres_extensions.models.fields.related import ArrayManyToManyField
#from django_postgres_extensions.models.fields.related import ArrayManyToManyField
#from django.contrib.postgres.forms import SplitArrayField
#from django_postgres_extensions.forms.fields import NestedFormField


class Studentarr(models.Model):
    i = models.IntegerField(blank=True, null=True)
    n = models.CharField(max_length = 50, blank=True, null=True)
    g = models.IntegerField(blank=True, null=True)
    #array = ArrayField(CharField(max_length = 50), IntegerField())
    class Meta:
        abstract = False


    #def __str__(self):
    #    return self.i

class StudentarrForm(forms.ModelForm):
     class Meta:
           model = Studentarr
           fields = ['i', 'n', 'g',]

def get_default_something():
    return {'list': []}


class Id(models.Model):
    i_d = models.IntegerField(primary_key = True, blank=True, null=False)
    name = models.CharField(max_length = 50, blank=True, null=True)
    last_name = models.CharField(max_length = 50, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    snipping = models.ForeignKey(Studentarr, related_name='a', on_delete=models.CASCADE)
    #student1 = models.EmbeddedField(model_container=Studentarr, model_form_class = StudentarrForm,)
    #shipping = HStoreField(keys=('Address', 'City', 'Region', 'Country'), blank=True, default=get_default_something)
    #snipping = HStoreField(null=True, blank=True)
    #snipping = JSONField(null=True, blank=True)
    #board = ArrayField(models.CharField(max_length=10, blank=True),size=8,)
    #board = ArrayField(models.IntegerField(),models.IntegerField(), null=True, blank=True, size=2)
    #student_array = models.ManyToManyField(Studentarr)
    #board = ArrayField(model_container=Studentarr)
    #board = models.ArrayField(model_container=Studentarr,)


'''
    def __str__(self):
        return self.id
        #return f"{self.name}:{self.last_name}"
'''

class Professions(models.Model):
    first_profession = models.CharField(max_length = 20)
    second_profession = models.CharField(max_length = 20)
    thrid_profession = models.CharField(max_length = 20)


class Adress(models.Model):
    city = models.CharField(max_length = 20)
    street = models.CharField(max_length = 20)
    num_home = models.IntegerField()
