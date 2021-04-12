from django.http import HttpRequest, HttpResponse, JsonResponse,QueryDict
from django.core.mail import send_mail
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import json

data = {
    'name': 'amirhossein',
    'family': 'hassniroshan',
    'password': '52608088',
    'email': 'rwshn938@gmail.com'
}


def home(request):
    return render(request, 'home.html')
