from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from . import models

def index(request):
    return HttpResponse("Hello, world. You're at the Nitro Backend index.")

@csrf_exempt
def handler(request):

    # only allow the HTTP POST method
    if request.method != 'POST':
         return HttpResponse("This endpoint only supports POST request.")

    # check if there are any files
    if request.FILES.get('photo', True) == True:
        return HttpResponse("This endpoint accepts multipart/form-data content, with field name 'photo'")


    # # Save Image
    image = models.Image(photo=request.FILES.get('photo'), processed_photo=request.FILES.get('photo'))
    image.detectshadow()
    result = image.compute()

    # Return response
    return JsonResponse(result)

   
