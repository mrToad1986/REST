# сериализация данных
# делаем json-представление из модели

from rest_framework.serializers import ModelSerializer
from .models import User


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('user_name', 'first_name', 'last_name', 'birthday_year', 'email')


class UserModelSerializerFull(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
#       all_fields = ('user_name', 'first_name', 'last_name', 'birthday_year', 'email', 'is_superuser', 'is_stuff')
