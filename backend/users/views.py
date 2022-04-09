from rest_framework.viewsets import GenericViewSet
from rest_framework import generics, permissions
from rest_framework import mixins
from .serializers import UserModelSerializer, UserModelSerializerFull
from .models import User
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class UserModelViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = UserModelSerializer
    queryset = User.objects.all()


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

    def get_serializer_class(self):
        if self.request.version == '1.2':
            return UserModelSerializerFull
        return UserModelSerializer

# class UserListAPIView(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserModelSerializer
#
#     def get_serializer_class(self):
#         if self.request.method in ['GET']:
#             return UserModelSerializerFull
#         return UserModelSerializer
