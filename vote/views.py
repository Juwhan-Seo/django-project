from django.shortcuts import render
from .models import vote 
# Create your views here.
def index(request):
    t = Topic.objects.all()
    c = Choice.objects.all()
    context = {
        "tset" : t
    }
    context = {
        "cset" : c
    }
    return render(request, "vote/index.html", context)


