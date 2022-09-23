from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from jonesandsons_pictures.models import Pictures
from jonesandsons_pictures.serializers import PicturesSerializer

# Create your views here.
def index(request):
    return HttpResponse("Hello world.")

@csrf_exempt
def picturesApi(request,id=0):
    if request.method=="GET":
        pictures = Pictures.objects.all()
        pictures_serializer = PicturesSerializer(pictures, many=True)
        return JsonResponse(pictures_serializer.data, safe=False)