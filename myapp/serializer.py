from rest_framework import serializers
from .models import *

class Clientserializer(serializers.ModelSerializer):
    class Meta:
        model=Client
        fields=("name","Created_by","Created_at")

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=("name","username","email","password1","password2")

class Projectserializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields=("name","user","client")
