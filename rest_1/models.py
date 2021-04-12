from django.db import models
from datetime import datetime


class book(models.Model):
    name = models.CharField(max_length=150)
    auth = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(default='', upload_to='upload_img/', null=True, blank=True)
    date = models.DateTimeField(datetime.now())

    def __str__(self):
        return self.name


class temp(models.Model):
    name = models.CharField(max_length=55)
    password = models.CharField(max_length=150)
    # image = models.ImageField(default='', upload_to='uplaod_img/', null=True, blank=True)
    file = models.FileField(default='', upload_to='upload_file/', null=True, blank=True)
    temp = models.IntegerField()

    def __str__(self):
        return "temp"
