from rest_framework import serializers

from .models import Variant


class ColorSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = '__all__'
