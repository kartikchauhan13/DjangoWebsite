from django.http import HttpResponse

def test(request):
    return HttpResponse("<h1>this is index</h1>")

def about(request):
    return HttpResponse("<h1>this is about page</h1>")

def services(request):
    return HttpResponse("<h1>this is service page</h1>")