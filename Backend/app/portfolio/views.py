from rest_framework import generics
from .serializers import *

# My Views


class SkillListView(generics.ListAPIView):
    serializer_class = SkillsListSerializer
    queryset = Skill.objects.all()


class TechListView(generics.ListAPIView):
    serializer_class = TechListSerializer
    queryset = Technology.objects.all()


class WorkListView(generics.ListAPIView):
    serializer_class = WorkListSerializer
    queryset = Work.objects.all()


class PersonListView(generics.ListAPIView):
    serializer_class = PersonListSerializer
    queryset = Person.objects.all()
