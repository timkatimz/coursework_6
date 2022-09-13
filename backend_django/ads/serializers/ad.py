from rest_framework import serializers

from ads.models import Ad


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class AdListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['pk', 'image', 'title', 'price', 'description']
