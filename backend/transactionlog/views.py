from django.http import HttpResponse
#from .models import Transaction


def index(request):
    return HttpResponse("Your transaction log will be here")