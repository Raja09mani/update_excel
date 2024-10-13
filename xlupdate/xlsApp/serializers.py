from rest_framework import serializers
from .models import StudDetail

class StudDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudDetail
        fields = '__all__'