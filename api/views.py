from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the Nitro Backend index.")

def handler(request):
    return HttpResponse("This is the handler")
