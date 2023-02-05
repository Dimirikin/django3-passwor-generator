from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, 'generater/home.html')

def password(request):

    characters = list('qwertyuiopasdfghjklzxcvbnm')

    if request.GET.get('uppercase'):
        characters.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length'))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generater/password.html', {'password': thepassword})

