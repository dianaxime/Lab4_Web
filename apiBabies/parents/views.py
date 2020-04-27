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

def evaluar(user, obj, request):
    return user.id == obj.user_id

class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='ParentPermission',
            permission_configuration={
                'base': {
                    #'create': True,
                    #'list': False,
                },
                'instance': {
                    'retrieve': evaluar,
                    #'destroy': False,
                    #'update': True,
                    #'partial_update': 'babies.change_baby',
                    'babies': evaluar,
                    # 'update_permissions': 'users.add_permissions'
                    # 'archive_all_students': phase_user_belongs_to_school,
                    # 'add_clients': True,
                }
            }
        ),
    )

    @action(detail=True, methods=['get'])
    def babies(self, request, pk=None):
        parent = self.get_object()
        return Response([BabySerializer(baby).data for baby in Baby.objects.filter(parent=parent)])
    