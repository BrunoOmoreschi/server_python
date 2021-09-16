import graphene
from graphene_django import DjangoObjectType
from users.schema import UserType
from .models import Link, Vote
from graphql import GraphQLError  # graphQL native error handling lib.
from django.db.models import Q  # for search / filtering entries.


class LinkType(DjangoObjectType):
    class Meta:
        model = Link


class VoteType(DjangoObjectType):
    class Meta:
        model = Vote


class Query(graphene.ObjectType):
    links = graphene.List(
        LinkType,
        search=graphene.String(),
        first=graphene.Int(),
        skip=graphene.Int(),
    )
    votes = graphene.List(VoteType)

    def resolve_links(self, info, search=None, first=None, skip=None, **kwargs):
        qs = Link.objects.all()

        # Lil block that calls for search if its in the query.
        if search:
            filter = (
                    Q(url__icontains=search) |
                    Q(description__icontains=search)
            )
            qs = qs.filter(filter)

        if skip:
            qs = qs[skip:]

        if first:
            qs = qs[:first]

        return qs

    # if there is no argument, lets return all the links.
    def resolve_votes(self, info, **kwargs):
        return Vote.objects.all()


class CreateLink(graphene.Mutation):
    id = graphene.Int()
    url = graphene.String()
    description = graphene.String()
    posted_by = graphene.Field(UserType)

    class Arguments:
        url = graphene.String()
        description = graphene.String()

    def mutate(self, info, url, description):
        user = info.context.user or None

        link = Link(
            url=url,
            description=description,
            posted_by=user,
        )
        link.save()

        return CreateLink(
            id=link.id,
            url=link.url,
            description=link.description,
            posted_by=link.posted_by,
        )


class CreateVote(graphene.Mutation):
    # Remember that is odd to allow a user to vote twice in a link,
    # so you must to implement a method in client to before use this mutation
    # check if there is a vote for this user.
    # I could implement it here? Yes. But I don't feel it right. See,
    # doing it here may create a dependency on the query code, or even a repeated
    # block of code. Instead of the client may shot a query for the votes on a desired
    # link with the context user. If there is none, call this method to create a vote.
    # If there is already a vote, you can handle with a warning, for example.
    user = graphene.Field(UserType)
    link = graphene.Field(LinkType)

    class Arguments:
        link_id = graphene.Int()

    def mutate(self, info, link_id):
        user = info.context.user
        if user.is_anonymous:
            # raise Exception('You must be logged to vote!')
            raise GraphQLError('You must be logged to vote!')

        link = Link.objects.filter(id=link_id).first()
        if not link:
            raise Exception('Invalid Link!')

        Vote.objects.create(
            user=user,
            link=link,
        )

        return CreateVote(user=user, link=link)


class DeleteLink(graphene.Mutation):
    # It will be cool to check if there is any vote on the link target,
    # if yes, deletion forbidden, if not proceed to execution.

    # The class attributes define the response of the mutation
    Link = graphene.Int()

    class Arguments:
        # The input arguments for this mutation
        id = graphene.ID()

    def mutate(self, info, id):
        link = Link.objects.get(id=id)
        if link is not None:
            link.delete()
        return DeleteLink(Link=link.id)


class DeleteVote(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.ID()
        link_id = graphene.ID()

    def mutate(self, info, id, link_id):
        vote = Vote.objects.get(id=id)

        # Check if the user is logged in.
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError('You must be logged to vote!')

        # Check if the link is valid.
        link = Link.objects.filter(id=link_id).first()
        if not link:
            raise GraphQLError('Invalid Link!')

        # Check if the vote is valid or xzqt the deletion.
        if vote is not None:
            vote.delete()
        else:
            raise GraphQLError('Invalid vote!')
        ok = True
        return DeleteVote(ok=ok)


class Mutation(graphene.ObjectType):
    create_link = CreateLink.Field()
    delete_link = DeleteLink.Field()

    create_vote = CreateVote.Field()
    delete_vote = DeleteVote.Field()
