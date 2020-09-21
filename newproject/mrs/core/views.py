from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer


# Create your views here.
import requests

def home(request):
    return JsonResponse({'main':'1'})

@api_view(('GET',))
def row(request):
    if request.method == "GET":
        r = requests.get("https://demo.openmrs.org/openmrs/ws/rest/v1/session")
        if r.status_code == 200:
            return Response(r,status=status.HTTP_200_OK)
    else:
        return Response({"error": "Method not allowed"}, status=status.HTTP_400_BAD_REQUEST)
