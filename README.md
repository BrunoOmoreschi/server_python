





```bash
pip install django graphene-django django-filter django-graphql-jwt
django-admin startproject hackernews
cd hackernews
python manage.py migrate
python manage.py runserver
```

Abrir outra instancia do Terminal,

Cd até a pasta raiz do projeto e dar o comando:

```bash
cd hackernews
```

```bash
python manage.py startapp lincks
```

Create the `lincks/schema.py` file, with the content below:

```python
import graphene
from graphene_django import DjangoObjectType

from .models import Link


class LinkType(DjangoObjectType):
    class Meta:
        model = Link


class Query(graphene.ObjectType):
    links = graphene.List(LinkType)

    def resolve_links(self, info, **kwargs):
        return Link.objects.all()
```



Vá no pyCharm menu File, Settings, linha 'Project Structure' e expanda até o nivel da pasta lincks. Clique com a direita na pasta hackernews e classifique ela como 'Excluded' assim ela fica como pasta que não fornece modulos de importação. Acontece que o próximo arquivo que vamos criar usará um modulo da lincks, mas o pycharm não localiza essa pasta até excluir a outra como fonte.

Create the `hackernews/schema.py` file, with the query type:

```python
import graphene

import lincks.schema


class Query(lincks.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
```





mutation {
  createLink(
    url: "http//github.com",
    description: "Lots of Code!"
  ){
    id
    url
    description
  }
}



query {
  links{
    id
    url
    description
  }
}
