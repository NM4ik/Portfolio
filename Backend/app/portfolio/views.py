from rest_framework import generics
from .serializers import *

# My Views


class SkillListView(generics.ListAPIView):
    serializer_class = SkillsListSerializer
    queryset = Skill.objects.all()
