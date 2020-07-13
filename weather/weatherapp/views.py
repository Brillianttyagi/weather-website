from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")
def fetchweather(request):
    country_name = request.GET['cname']
    state_name = request.GET['ciname']
    d = state_name
    return render(request,'result.html',{'city':d})