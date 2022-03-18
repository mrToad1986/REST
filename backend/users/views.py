from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from .serializers import UserModelSerializer
from .models import User

class UserModelViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin, GenericViewSet):
    serializer_class = UserModelSerializer
    queryset = User.objects.all()