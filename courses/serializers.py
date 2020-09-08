# Serializer ; converting database to and from json
from rest_framework import serializers

from .models import Course

class CourseSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model  = Course
    fields = ('id', 'url', 'name', 'language', 'price')