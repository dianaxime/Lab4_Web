from django.shortcuts import render

# Create your views here.
from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from permissions.services import APIPermissionClassFactory
from parents.models import Parent
from parents.serializers import ParentSerializer
from babies.models import Baby
from babies.serializers import BabySerializer


class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

    @action(detail=True, methods=['get'])
    def babies(self, request, pk=None):
        parent = self.get_object()
        return Response([BabySerializer(baby).data for baby in Baby.objects.filter(parent=parent)])
    