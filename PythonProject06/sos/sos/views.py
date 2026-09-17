from django.http import HttpResponse


def test(request):
    return HttpResponse(request,'<h1>sos test is running</h1>')