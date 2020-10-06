#renders a template displaying the current date and time
from django.shortcuts import render, HttpResponse, redirect
#to import timestamp functionality
from time import gmtime, strftime

#BONUS: Come up with a different way to retrieve the datetime
from datetime import datetime

# Create your views here.
def redir(request):
    return redirect ('/')

def index(request):
    #create a dictionary to pass the user's current time
    context = {
        "time" : strftime("%b, %d %Y %H:%M %p", gmtime())
    }
    return render(request, 'index.html', context)

#BONUS: Come up with a different way to retrieve the datetime
def bonus(request):
    context={
        'dt_time' : datetime.now()
    }
    return render(request, "index.html", context)