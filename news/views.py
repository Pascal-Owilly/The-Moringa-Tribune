from django.shortcuts import render
from django.http import HttpResponse, Http404
import datetime as dt

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to Moringa')


def news_of_day(request):
    date = dt.date.today()
    # Convert date object to find the eaxct date
    day = convert_date(date)
    return render(request, 'welcome.html')

def convert_date(dates):
    # get wekday number for the date
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thurday','Friday','Saturday','Sunday']

    # Returning the actual day
    day = days[day_number]
    return day

def past_days_news(request, past_date):

    try:
        # Converts data from the string url
        date = dt.datetime.strftime(past_date, '%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error 
        raise Http404()
    day = convert_date(date)

    return render(request, 'welcome.html')


   