from rest_framework import serializers
from . import models


class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'is_admin',
        ]


class CustomUserListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'is_admin',
        ]
