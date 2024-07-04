from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import Group, Permission
from .models import Address, UserProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'username', 'email', 'first_name', 'last_name','password']
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        user = authenticate(username=username, password=password)

        if user:
            return user
        else:
            raise serializers.ValidationError('Invalid credentials')


class AddressSerializer(serializers.ModelSerializer):
    customer = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Address
        fields = ('id', 'street', 'city', 'postal_code', 'customer')


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['phone', 'birth_date', 'membership', 'customer_image']
