from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from .serializers import UserModelSerializer
from .models import User
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class UserModelViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = UserModelSerializer
    queryset = User.objects.all()