from django.http import JsonResponse

from django.core.exceptions import BadRequest
from django.views.decorators.csrf import csrf_exempt

from . import models

from .shadowDetection import shadowDetection

@csrf_exempt
def handler(request):
    # only allow the HTTP POST method
    if request.method != 'POST':
        raise BadRequest("This endpoint does not support " + request.method + " HTTP method.")

    # check if there are any files
    if request.FILES.get('photo', True) == True:
        raise BadRequest("This endpoint accepts multipart/form-data content, with field name 'photo'")


    # Save Image
    image = models.Image(photo=request.FILES.get('photo'), processed_photo=request.FILES.get('photo'))
    image.detectshadow()
    result = image.compute()

    # Return response
    return JsonResponse(result)