from rest_framework import serializers
from .models import MapFlag

class MapFlagSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapFlag
        fields = ('id','status')

    def create(self, validated_data):
        return MapFlag.objects.create(**validated_data)

    def update(self, instance, validated_data):
        print(instance)
        print(validated_data.get('id', instance.id))
        instance.id = validated_data.get('id', instance.id)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance