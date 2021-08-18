from rest_framework import serializers
from .models import *


class TechListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = "__all__"


class SkillsListSerializer(serializers.ModelSerializer):
    tech_id = TechListSerializer(many=True, read_only=True)

    class Meta:
        model = Skill
        fields = "__all__"


class WorkListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = "__all__"


class PersonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"
