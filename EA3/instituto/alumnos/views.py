from django.shortcuts import render

def index(request):
    context={}
    return render('alumnos/index.html', context)

# Create your views here.
