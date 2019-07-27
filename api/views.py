from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status, generics

from nameparser import HumanName
from configparser import RawConfigParser

from .serializers import MapFlagSerializer
from .models import MapFlag

import os
from django.conf import settings


# Create your views here.

class GetStatus(APIView):
    def get(self, request):
        print(settings.BASE_DIR)
        file_ = os.path.join(settings.BASE_DIR, 'config.ini')
        config = RawConfigParser()
        config.read(r''+file_)
        request.data['mapflagstatus'] = config.get('mapflag', 'status')
        return Response(request.data, status=status.HTTP_201_CREATED)

    def post(self, request, format=None):
        mapflagstatus = request.data['mapflagstatus']
        file_ = os.path.join(settings.BASE_DIR, 'config.ini')
        config = RawConfigParser()
        config.read(r'' + file_)
        if mapflagstatus == True or mapflagstatus == 'True':
            config['mapflag']['status'] = 'True'
        else:
            config['mapflag']['status'] = 'False'
        with open(r'' + file_, 'w') as configfile:
            config.write(configfile)
        config = RawConfigParser()
        config.read(r'' + file_)
        request.data['mapflagstatus'] = config.get('mapflag', 'status')
        return Response(request.data, status=status.HTTP_201_CREATED)


class GetHumanNameParser(APIView):
    def post(self, request, format=None):
        name = HumanName(str(request.data['name']))
        request.data['response'] = name.as_dict()
        return Response(request.data, status=status.HTTP_201_CREATED)


class MapFlagAPI(APIView):

    def get(self, request):
        # flagdata = MapFlag.objects.all()
        usernames = [user.status for user in MapFlag.objects.all()]
        print(usernames)
        return Response([{"status": usernames}])

    def post(self, request, format=None):
        print(request.data)
        serializerData = MapFlagSerializer(data = request.data)
        if serializerData.is_valid():
            d = serializerData.save()
            request.data['id'] = d.pk
        return Response(request.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk=None):
        FlagData = get_object_or_404(MapFlag.objects.all(), pk=pk if pk != None else request.data['id'])
        print(FlagData)
        print(request.data)
        data = request.data
        serializer = MapFlagSerializer(instance=MapFlag, data=data, partial=True)
        serializer.save()
        if serializer.is_valid(raise_exception=True):
            d = serializer.save()
        return Response(request.data, status=status.HTTP_201_CREATED)
