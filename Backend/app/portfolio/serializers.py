from rest_framework import serializers
from .models import *


class SkillsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"
