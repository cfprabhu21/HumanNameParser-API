from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status, generics

from nameparser import HumanName

from .serializers import MapFlagSerializer
from .models import MapFlag

# Create your views here.

class GetHumanNameParser(APIView):
    def post(self, request, format=None):
        name = HumanName(str(request.data['name']))
        request.data['response'] = name.as_dict()
        return Response(request.data, status=status.HTTP_201_CREATED)


class MapFlagAPI(APIView):

    def get(self, request):
        flagdata = MapFlag.objects.all()
        return Response({"flagdata": flagdata})

    def post(self, request, format=None):
        print(request.data)
        serializerData = MapFlagSerializer(data = request.data)
        if serializerData.is_valid():
            d = serializerData.save()
            request.data['id'] = d.pk
        return Response(request.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk=None):
        FlagData = get_object_or_404(MapFlag.objects.all(), pk=pk if pk != None else request.data['id'])
        data = request.data
        serializer = MapFlagSerializer(instance=MapFlag, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            d = serializer.save()
        return Response(request.data, status=status.HTTP_201_CREATED)
