import apps.users.schema 
import graphene

from graphene_django.debug import DjangoDebug

class Query(
    apps.users.schema.Query,
    graphene.ObjectType,
):
    debug = graphene.Field(DjangoDebug, name="_debug")

class Mutation(
    apps.users.schema.Mutation,
    graphene.ObjectType,
):
    debug = graphene.Field(DjangoDebug, name="_debug")

schema = graphene.Schema(query=Query,mutation=Mutation)