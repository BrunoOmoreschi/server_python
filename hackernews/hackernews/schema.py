import graphene
import graphql_jwt
import users.schema
import lincks.schema
import lincks.schema_relay


class Query(
    users.schema.Query,
    lincks.schema.Query,
    lincks.schema_relay.RelayQuery,
    graphene.ObjectType,
):
    pass


class Mutation(
    users.schema.Mutation,
    lincks.schema.Mutation,
    lincks.schema_relay.RelayMutation,
    graphene.ObjectType,
):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
