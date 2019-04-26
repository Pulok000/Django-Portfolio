# Create your views here.


'''from django.http import HttpResponse

httpresponse is responseable for showing stuff on browser

def myfunction(anyting):
    return HttpResponse("OWWW, ITS CELEBRATION TIMEZ")'''

from django.shortcuts import render

import requests, json

from .models import contact, student


def pokafun(request):
    if request.method == 'POST':
        name1 = request.POST.get('fname')
        name2 = request.POST.get('lname')
        a = student(first_name=name1, last_name=name2)
        a.save()
        p = requests.get('http://api.icndb.com/jokes/random?firstName=' + name1 + '&lastName=' + name2)
        json_data = json.loads(p.text)
        joke = json_data.get('value').get('joke')

        maincotain = {'joker': joke}

        # print(joke)

        return render(request, 'my1stapp/index.html', maincotain)
    else:
        name1 = 'pulok'
        name2 = 'Ahmed'

        p = requests.get('http://api.icndb.com/jokes/random?firstName=' + name1 + '&lastName=' + name2)
        json_data = json.loads(p.text)
        joke = json_data.get('value').get('joke')

        maincotain = {'joker': joke}
        return render(request, 'my1stapp/index.html',maincotain)


def portfolio(request):
    return render(request, 'my1stapp/portfolio.html')


def Contact(request):
    if request.method == 'POST':
        # print(request.POST.get('email'))
        email_r = request.POST.get('email')
        subject_r = request.POST.get('subject')
        message_r = request.POST.get('message')
        c = contact(email=email_r, subject=subject_r, message=message_r)
        c.save()
        return render(request, 'my1stapp/thankyou.html')
    else:
        return render(request, 'my1stapp/contact.html')
