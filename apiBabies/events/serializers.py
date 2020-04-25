from rest_framework import serializers

from events.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            'id',
            'type',
            'note',
            'date',
            'owner'
        )