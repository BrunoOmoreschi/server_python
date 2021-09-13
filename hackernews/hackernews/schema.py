import graphene

import lincks.schema


class Query(lincks.schema.Query, graphene.ObjectType):
    pass


class Mutation(lincks.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
