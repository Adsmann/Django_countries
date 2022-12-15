import json
from urllib import response

from django.contrib.sites import requests
from django.db import models
from django.http import JsonResponse, HttpResponse


class Countrys(models.Model):
    country= models.TextField('Страна')
    languages= models.TextField('Языки')

    def __str__(self):
        return self.country