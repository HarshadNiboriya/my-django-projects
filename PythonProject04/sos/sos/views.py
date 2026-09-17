from django.http import HttpResponse

def test(request):
    return HttpResponse('<h1>sos views test function</h1>')
