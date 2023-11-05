from .models import *
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=[
            'id',
            'name',
            'title',
            'description',
            'slug',
            'views',
            'students',
            'type'
        ]