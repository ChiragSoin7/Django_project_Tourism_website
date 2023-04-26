from django.shortcuts import render,HttpResponse
from datetime import datetime
from shanu.models import Contact
from .utils import get_weather_data
import requests
import datetime
# Create your views here.
def index(request):
    context ={
        'variable':'hy my name is yo'
    }
    return render(request,'home.html',context)
    # return HttpResponse("this is shanu")
def about(request):
    return render(request,'about.html')
def jaipur(request):
    return render(request,'jaipur.html')
def weather(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city='jaipur'
    appid ='c1ec97e11969f94f89436bf33109d638'
    URL ='https://api.openweathermap.org/data/2.5/weather'
    PARAMS={'q': city,'appid':appid,'units':'metric'}
    r=requests.get(url=URL,params=PARAMS)
    res=r.json()
    description =res['weather'][0]['description']
    icon =res['weather'][0]['icon']
    temp =res['main']['temp']
    day=  datetime.date.today()

    return render(request,'weather.html',{'description':description,'icon':icon,'temp':temp,'day':day,'city':city})
    # return HttpResponse("hello i m about")
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email =request.POST.get('email')
        phone= request.POST.get('phone')
        desc = request.POST.get('desc')
        contact1 = Contact(name=name , email=email ,phone=phone , desc=desc , date=datetime.today())
        contact1.save()
    
    return render(request,'contact.html')
    # return HttpResponse("this is contact")
def services(request):
    return render(request,'services.html')
    # return HttpResponse("this is services")
def services2(request):
    return render(request,'services2.html')
def services3(request):
    return render(request,'services3.html')
def jodh(request):
    return render(request,'jodh.html')
def jaisal(request):
    return render(request,'jesal.html')
def pali(request):
    return render(request,'pali.html')
def udaipur(request):
    return render(request,'udai.html')
def kota(request):
    return render(request,'kota.html')
def bikaner(request):
    return render(request,'bika.html')
def bharatpur(request):
    return render(request,'bhrt.html')
def alwar(request):
    return render(request,'alwar.html')
