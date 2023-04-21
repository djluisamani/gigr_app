from django.db import models

class Gig(models.Model):
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    venue = models.CharField(max_length=255)
    event_type = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=255)

class Payment(models.Model):
    gig = models.ForeignKey(Gig, on_delete=models.CASCADE)
    amount = models.FloatField()
    date = models.DateField()
    method = models.CharField(max_length=255)

class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    notes = models.TextField()
