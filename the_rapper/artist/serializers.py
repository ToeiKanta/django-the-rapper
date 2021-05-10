from rest_framework import serializers
from .models import Artist

class ArtistSerializer(serializers.ModelSerializer):
  class Meta:
    model = Artist
    fields = '__all__'


class ArtistSaveSerializer(serializers.ModelSerializer):
  class Meta:
    model = Artist
    fields = 'aka','name','age'