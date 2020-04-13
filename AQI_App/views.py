from django.shortcuts import render
from django.http import HttpResponse
from lib.bs4 import BeautifulSoup
import numpy
import urllib.request as url

def fetchCityIndex(cityName):
    if cityName=='Delhi':
        cityHtml= url.urlopen("https://www.aqi.in/dashboard/india/delhi/new-delhi").read()
    if cityName=='Ahmedabad':
        cityHtml= url.urlopen("https://www.aqi.in/dashboard/india/gujarat/ahmedabad").read()
    if cityName=='Bengaluru':
        cityHtml= url.urlopen("https://www.aqi.in/dashboard/india/karnataka/bengaluru").read()
    if cityName=='Mumbai':
        cityHtml= url.urlopen("https://www.aqi.in/dashboard/india/maharashtra/mumbai").read()
    if cityName== 'Pune':
        cityHtml= url.urlopen("https://www.aqi.in/dashboard/india/maharashtra/pune").read()
    if cityName== 'Chennai':
        cityHtml= url.urlopen("https://www.aqi.in/dashboard/india/tamilnadu/chennai").read()
    if cityName== 'Hyderabad':
        cityHtml= url.urlopen("https://www.aqi.in/dashboard/india/telangana/hyderabad").read()
    if cityName== 'Kolkatta':
        cityHtml= url.urlopen("https://www.aqi.in/dashboard/india/west-bengal/kolkata").read()
    soup = BeautifulSoup(cityHtml, 'html.parser')
    try:
        for j in soup.findAll("div", {"class": "sectot-box-left"}):
            for k in j.findAll('h2'):
                cityIndex=k.text
            for m in j.findAll('h3'):
                cityLevel=m.text
    except:
        print("No a tags")
    return cityName+": "+cityIndex+" - "+cityLevel

def cityIndex(request):
    if request.method == "POST":
        cityName = request.POST['Cities']
        cityIndex=fetchCityIndex(cityName)
        Context = {
            'CityIndx': cityIndex
        }
    return render(request,'AQI_App/Context.html',Context)

def index(request):
    return render(request,'AQI_App/AQI.html')
