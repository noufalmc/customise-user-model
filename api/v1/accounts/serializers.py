from django.contrib.auth import authenticate
from rest_framework import serializers
from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'address']

        def save(self, validated_data, **kwargs):
            user = User.object.create_user(first_name=validated_data.data.get('first_name'),
                                           last_name=validated_data.data.get('last_name'),
                                           email=validated_data.data.get('email'),
                                           password=validated_data.data.get('password'),
                                           address=validated_data.data.get('address')
                                           )
            return user


