from django.shortcuts import render
from .models import Place

# Create your views here.

def demo(home):
    obj = Place.objects.all()
    # new_1 = assignment.objects.all()
    return render(home, 'index.html', {'files': obj})