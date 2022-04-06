from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to Moringa')


def news_of_day(request):
    date = dt.date.today()
    # Convert date object to find the eaxct date
    day = convert_date(date)
    html = f'''
        <html>
            <body>
                <h1> News for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)

def convert_date(dates):
    # get wekday number for the date
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thurday','Friday','Saturday','Sunday']

    # Returning the actual day
    day = days[day_number]
    return day

   