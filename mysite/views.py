from django.http import HttpResponse

def home(request):
    return HttpResponse('<h3>Hello, Django! This is our home page</h3>')