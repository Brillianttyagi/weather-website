from django.shortcuts import render
from django.http import HttpResponse
import requests, json 

# Create your views here.
def index(request):
    return render(request, "index.html")
def fetchweather(request):
    country_name = request.GET['cname']
    state_name = request.GET['ciname']
    # Python program to find current  
    # weather details of any city 
    # using openweathermap api 
    
    
    # Enter your API key here 
    api_key = "ae2133856e39811ef46152ca3d72b3d2"
    
    # base_url variable to store url 
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    # Give city name 
    city_name = state_name
    
    # complete_url variable to store 
    # complete url address 
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
    
    # get method of requests module 
    # return response object 
    response = requests.get(complete_url) 
    
    # json method of response object  
    # convert json format data into 
    # python format data 
    x = response.json() 
    
    # Now x contains list of nested dictionaries 
    # Check the value of "cod" key is equal to 
    # "404", means city is found otherwise, 
    # city is not found 
    if x["cod"] != "404": 
        requestb=True
        # store the value of "main" 
        # key in variable y 
        y = x["main"] 
    
        # store the value corresponding 
        # to the "temp" key of y 
        current_temperature = y["temp"] 
    
        # store the value corresponding 
        # to the "pressure" key of y 
        current_pressure = y["pressure"] 
    
        # store the value corresponding 
        # to the "humidity" key of y 
        current_humidiy = y["humidity"] 
    
        # store the value of "weather" 
        # key in variable z 
        z = x["weather"] 
    
        # store the value corresponding  
        # to the "description" key at  
        # the 0th index of z 
        weather_description = z[0]["description"] 
        return render(request,'result.html',{'request':requestb,'country':country_name,'city':state_name,'temp':current_temperature,'pre':current_pressure,'hum':current_humidiy,'des':weather_description})
    
    else: 
        requestb = False
        return render(request,'result.html',{'request':requestb,'country':country_name,'city':state_name})