from rest_framework import serializers
from .models import MapFlag

class MapFlagSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapFlag
        fielde = ('flag')

    def create(self, validated_data):
        return MapFlag.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.responsedata = validated_data.get('responsedata', instance.responsedata)
        instance.datemodified = validated_data.get('datemodified', instance.datemodified)
        instance.save()
        return instance