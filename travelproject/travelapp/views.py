from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Team


# Create your views here.

def demo(request):
    plc = Place.objects.all()
    tem = Team.objects.all()
    return render(request, "index.html", {'Place': plc,
                                          'Team': tem})





#def about(request):
#    return render(request, "about.html")

#def contact(request):
#   return HttpResponse("hello am contact")