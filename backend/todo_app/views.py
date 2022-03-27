from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Project, TODO
from .serializers import ProjectModelSerializer, TODOModelSerializer
from .filters import ProjectFilter, TODOFilter


# class ProjectLimitOffsetPagination(LimitOffsetPagination):
#     default_limit = 10
#
#
# class TODOLimitOffsetPagination(LimitOffsetPagination):
#     default_limit = 20


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    filterset_class = ProjectFilter
    # pagination_class = ProjectLimitOffsetPagination


class TODOModelViewSet(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOModelSerializer
    filterset = TODOFilter
    # pagination_class = TODOLimitOffsetPagination
    def perform_destroy(self, request, pk = None, **kwargs):
        todo = get_object_or_404(TODO, pk=pk)
        todo.is_active = False
        todo.save()
        return Response(TODOModelSerializer(todo, context={'request': request}).data)
