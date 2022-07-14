import datetime

from dateutil.relativedelta import relativedelta
from django.db import models
from django.urls import reverse


# Create your models here.

# class Users(models.Model):
#     login = models.CharField(max_length=60)
#     password = models.CharField(max_length=100)

class Clients(models.Model):
    name = models.CharField(max_length=30, null=True)
    surname = models.CharField(max_length=30, default='', null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=30, default='', null=True, blank=True)
    adress = models.CharField(max_length=100, default='', null=True, blank=True)
    bith = models.DateField(null=True, blank=True)
    info = models.CharField(max_length=150, default='', null=True, blank=True)

    class Meta:
        ordering = ['name', 'surname']

    def __str__(self):
        return f"{self.name} {self.surname}" if self.surname != None else f"{self.name}"

    def get_url(self):
        return reverse("client_detail", args=[self.pk])

    # @property
    # def babys(self):
    #     a = (datetime.datetime.now().date() - self.bith).days
    #     years = int(a // 365.25)
    #     mounth = int((a % 365.25) // 30)
    #     # a = int((datetime.datetime.now().date() - self.bith).days / 365.25)
    #     return "Newborn"


class Babys(models.Model):
    name = models.CharField(max_length=30)
    bith = models.DateField(null=True, blank=True)
    parent = models.ForeignKey(Clients, on_delete=models.SET_NULL, null=True, blank=True)

    def get_url(self):
        return reverse("baby_detail", args=[self.pk])

    @property
    def age(self):
        a = (datetime.datetime.now().date() - self.bith).days
        years = int(a // 365.25)
        mounth = int((a % 365.25) // 30)
        # a = int((datetime.datetime.now().date() - self.bith).days / 365.25)
        if years > 0:
            return f"{years} years, {mounth} month" if years > 1 else f"{years} year, {mounth} month"
        elif mounth > 0:
            return f"{mounth} month"
        else:
            return "Newborn"

    # age = property(calculate_age)


class Services(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse("service_detail", args=[self.pk])


class Status(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Orders(models.Model):
    date = models.DateField()
    price = models.IntegerField()
    info = models.CharField(max_length=120, default='', null=False, blank=True)
    client = models.ForeignKey(Clients, on_delete=models.SET_NULL, null=True, blank=True)
    service = models.ForeignKey(Services, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.ForeignKey(Status, default=1, on_delete=models.SET_NULL, null=True, blank=True)

    # client = models.IntegerField(null=True, blank=True)
    # service = models.IntegerField(null=True, blank=True)
    # status = models.IntegerField(null=True, blank=True)
    def get_url(self):
        return reverse("order_detail", args=[self.pk])


# site part

class Reviews(models.Model):
    name = models.CharField(max_length=40)
    photo = models.CharField(max_length=30)
    text = models.TextField()
    show = models.BooleanField()
    newborn = models.BooleanField()
