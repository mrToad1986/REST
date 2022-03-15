from rest_framework.serializers import ModelSerializer, StringRelatedField
from backend.users.models import User
from backend.users.serializers import UserModelSerializer
from models import Project, TODO


class UserListModelSerializer(UserModelSerializer):
    class Meta:
        model = User
        fields = ('user_name', 'first_name', 'last_name', 'birthday_year', 'email')


class ProjectModelSerializer(ModelSerializer):
    users = UserListModelSerializer(many=True)

    class Meta:
        model = Project
        fields = ('name', 'ref', 'users')


class TODOModelSerializer(ModelSerializer):
    user = StringRelatedField()
    project = StringRelatedField()

    class Meta:
        model = TODO
        exclude = ('id',)