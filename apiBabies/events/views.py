from django.shortcuts import render

# Create your views here.
from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from permissions.services import APIPermissionClassFactory
from events.models import Event
from events.serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='EventPermission',
            permission_configuration={
                'base': {
                    'create': True,
                    'list': False,
                },
                'instance': {
                    'retrieve': 'events.view_event',
                    'destroy': False,
                    'update': False,
                    'partial_update': 'events.change_event',
                    #'notify': evaluar_notify,
                    # 'update_permissions': 'users.add_permissions'
                    # 'archive_all_students': phase_user_belongs_to_school,
                    # 'add_clients': True,
                }
            }
        ),
    )

    def perform_create(self, serializer):
        babyId = serializer.validated_data["babyId"]
        user = self.request.user
        userId = str(user.id)
        babyId = str(babyId)
        if babyId == userId:
            event = serializer.save()
            assign_perm('events.change_event', user, event)
            assign_perm('events.view_event', user, event)
            return Response(serializer.data)
        else:
            return Response({
                'ERROR': 'Usted no es el padre de ese bebe'
            })


        