from django.shortcuts import render
from . import models


# Create your views here.
def view_cnf(request):
    args = {'conferences': models.Conference.objects.all()}
    return render(request, 'conference/conferences.html', args)


def buy_ticket(request):
    return render(request, 'conference/buy_ticket.html')
