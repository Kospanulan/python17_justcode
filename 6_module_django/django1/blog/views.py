from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def index(request, *args, **kwargs):
    # return HttpResponse("Hello World!")
    return JsonResponse({"detail": "Hello World!"})
