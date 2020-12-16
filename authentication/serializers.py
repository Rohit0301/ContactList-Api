from rest_framework import serializers
from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=60,min_length=8,write_only=True)
    email=serializers.EmailField(max_length=55,min_length=6)
    first_name=serializers.CharField(max_length=60,min_length=2)
    last_name=serializers.CharField(max_length=60,min_length=2)


    class Meta:
        model=User
        fields=['username','first_name','last_name','email']

    def validate(self,attrs):
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({'email',('Email already exists')})

        return super().create(validated_data)

    def create(self,validated_data):
        return User.objects.create_user(validated_data)
