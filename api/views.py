from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status, generics

from nameparser import HumanName

# Create your views here.

class GetHumanNameParser(APIView):
    def post(self, request, format=None):
        name = HumanName(str(request.data['name']))
        request.data['response'] = name.as_dict()
        return Response(request.data, status=status.HTTP_201_CREATED)
