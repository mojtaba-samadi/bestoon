from django.shortcuts import render, HttpResponse
from web.models import *
import datetime

# Create your views here.

def submit_income(request):
    #print("salam\n\n\n\n\n\n\n")
    token = request.POST['token']
    this_user = User.objects.filter(token__token = this_token).get()
    if 'date' not in request.POST:
        now = datetime.datetime.now()
    Expense.objects.Create(user=this_user, amount=request.POST['amount'],
    text = request.POST['text'],date=now)

    return HttpResponse(request.POST['token'])


def submit_expense(request):
    #print("salam\n\n\n\n\n\n\n")
    token = request.POST['token']
    this_user = User.objects.filter(token__token = this_token).get()
    if 'date' not in request.POST:
        now = datetime.datetime.now()
    now = datetime.datetime.now()
    Income.objects.Create(user=this_user, amount=request.POST['amount'],
    text = request.POST['text'],date=now)

    return HttpResponse(request.POST['token'])
