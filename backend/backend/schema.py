import graphene
from graphene_django import DjangoObjectType
from todo_app.models import Project, TODO
from users.models import User

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'

class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'

class TODOtype(DjangoObjectType):
    class Meta:
        model = TODO
        fields = '__all__'

class Query(graphene.ObjectType):
    hello = graphene.String(default_value='Hello!')

    all_users = graphene.List(UserType)

    def resolve_all_users(root, info):
        return User.objects.all()

    user_by_id = graphene.Field(UserType, pk=graphene.Int(required=True))

    def resolve_user_by_id(root, info, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return None

    all_projects = graphene.List(ProjectType)

    def resolve_all_projects(root, info):
        return Project.objects.all()

    all_TODO = graphene.List(TODOtype)

    def resolve_all_TODO(root, info):
        return TODO.objects.all()

schema = graphene.Schema(query=Query)
