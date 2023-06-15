from rest_framework import serializers

from .models import Positions, Sections


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sections
        fields = "__all__"


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Positions
        fields = "__all__"
