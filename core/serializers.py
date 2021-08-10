from rest_framework import serializers
from . import models


class SeatQuestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'is_admin',
        ]


class SeatQuestListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'is_admin',
        ]
