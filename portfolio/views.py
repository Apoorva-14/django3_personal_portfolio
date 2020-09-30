from django.shortcuts import render
from .models import Info

def home(request):
    infos = Info.objects.all()
    return render(request,'portfolio/home.html', {'infos':infos})
