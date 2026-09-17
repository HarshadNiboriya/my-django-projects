
from django.http import HttpResponse

def display(request):
    return HttpResponse('<h1><b>welcome to sos views display function</b></h1>')