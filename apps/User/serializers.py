from rest_framework import serializers
from .models import User
import re
from django.core.exceptions import ValidationError


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'phone']
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 6, 'max_length': 20 }
        }
    
    # Проверка на корректность пароля
    def validate_password(self, value):
        if not re.match(r'^(?=.*[A-Za-z])(?=.*\d)', value):
            raise serializers.ValidationError("Пароль должен содержать как минимум одну букву и одну цифру")
        return value
    
