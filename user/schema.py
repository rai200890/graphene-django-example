from graphene import Node, ObjectType, Schema, Interface
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from user.models import User


class NodeInterface(Interface):

    @classmethod
    def get_node(cls, info, id):
        node = cls._meta.model.objects.get(id)
        return node


class UserType(DjangoObjectType, NodeInterface):

    class Meta:
        model = User
        interfaces = (Node, )
        filter_fields = {
            "name": ["exact", "icontains", "istartswith"],
            "email": ["exact"]
        }


class UserQuery(ObjectType):
    user = Node.Field(UserType)
    users = DjangoFilterConnectionField(UserType)


class Query(UserQuery):
    pass


schema = Schema(query=Query)
