from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
   people = [
      {
         "name":"ram",
         "age":"25",
         "contact":"98546225555"
      },
      {
         "name":"abc",
         "age":"60",
         "contact":"98546225555"
      },
      {
         "name":"ert",
         "age":"50",
         "contact":"98546225555"
      },
      {
         "name":"ffg",
         "age":"30",
         "contact":"98546225555"
      },
      {
         "name":"ffg",
         "age":"30",
         "contact":"98546225555"
      },
      {
         "name":"ffg",
         "age":"30",
         "contact":"98546225555"
      }
   ]
   context = {
      "title": "HOME Page",
      "body":"!!!!",
      "PEOPLE": people
   }
   return render(request,'home.html',context)

# home()


def about_us(request):
    context = {
        "title":"About-us",
        "body":"I am Nischal"
    }
    return render(request, 'about_us.html', context)
   


def contact_us(request):
    context = {
        "title":"contact-us",
        "body":"parajulinischal204@gmail.com"
    }
    return render(request, 'contact_us.html', context)
