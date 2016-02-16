__author__ = 'jjh'

from rest_framework import serializers
from api.models import User, DDrop


class UserSerializer(serializers.ModelSerializer):
    """
    This class will serialize User instances in the database into JSON format
    """

    class Meta:
        model = User
        fields = ('user_id', 'name', 'surname', 'email')


class DropSerializer(serializers.ModelSerializer):
    """
    This class will serialize DDrop instances in the database into JSON format
    """

    class Meta:
        model = DDrop
        fields = ('drop_id', 'submitter_id', 'latitude', 'longitude', 'data',
                  'date_dropped')

