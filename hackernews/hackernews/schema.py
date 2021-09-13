import graphene
import users.schema
import lincks.schema


class Query(users.schema.Query, lincks.schema.Query, graphene.ObjectType):
    pass


class Mutation(users.schema.Mutation, lincks.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
