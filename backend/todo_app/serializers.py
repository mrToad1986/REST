from rest_framework.serializers import ModelSerializer, StringRelatedField, HyperlinkedModelSerializer
from users.models import User
from users.serializers import UserModelSerializer
from .models import Project, TODO


class UserListModelSerializer(UserModelSerializer):

    class Meta:
        model = User
        fields = ('user_name', 'first_name', 'last_name', 'birthday_year', 'email')


class TODOListSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = TODO
        fields = ('project', 'update_at', 'is_active')


class ProjectModelSerializer(ModelSerializer):
    users = UserListModelSerializer(many=True)
    todo_list = TODOListSerializer(many=True)

    class Meta:
        model = Project
        fields = ('name', 'ref', 'users', 'todo_list')


class TODOModelSerializer(HyperlinkedModelSerializer):
    user = StringRelatedField()
    project = StringRelatedField()

    class Meta:
        model = TODO
        fields = '__all__'
