from django.db import models

from django_better_repr import better_repr

# Create your models here.


class JustForFKs(models.Model):
    ...


class JustForM2Ms(models.Model):
    ...


@better_repr
class FourOrLessFields(models.Model):
    one = models.CharField(max_length=16)
    two = models.CharField(max_length=32, default='Default', null=True)
    three = models.IntegerField(null=True)
    four = models.ForeignKey(to=JustForFKs, on_delete=models.CASCADE)


@better_repr
class FourOrMoreFields(models.Model):
    one = models.CharField(max_length=16)
    two = models.CharField(max_length=32, default='Default', null=True)
    three = models.IntegerField(null=True)
    four = models.ForeignKey(to=JustForFKs, on_delete=models.CASCADE)
    five = models.ManyToManyField(to=JustForM2Ms)
    six = models.FloatField()


class WithoutDecorator(models.Model):
    one = models.CharField(max_length=16)
    two = models.CharField(max_length=32, default='Default', null=True)
