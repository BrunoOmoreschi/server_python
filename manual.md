![header](https://github.com/BrunoOmoreshi/server_python/blob/main/header.png)

# Introduction

This project is the result of following the official tutorial for a server for backend clone of a blog called "Hacker News".

The link of tutorial is: https://www.howtographql.com/graphql-python/0-introduction/ 

But there are some implementations beyond the tutorial in order to accomplish a full CRUD application. This means that one may find functions to update and delete, what is not available on the site.

Also some architecture refactoring is going. This is because on the original material the links and votes share one schema file, but the users have its own schema definition file. Doing so the code is against some principles like SOLID, because one can not only use the vote class and methods without the file where the links definitions are, even if it doesn't have nothing to do with that.

# Usage

Here we can find the posts you may need in order to use the server once it is installed in your instance.

I'm using Insomnia to make the querys and mutations. But already tested the project responses on VS Code by the Thunder Client extension. You may use Postman too, or develop your own client following any tutorial on How to GraphQL.

Being a GraphQL server one can retrieve the information as requested by the client. In this manual all the possible field available will be in the examples. To see how to customize your client to get only what you want please look for the official documentation.

## Authorization header

To perform some operations you need to be logged in. To do so, you will need a User (please refer to User section on this very guide) and use its token on header. Create a header named: "AUTHORIZATION". On the value put "JWT xxxxxxx", change the xxxxxx by your token.

## Links

Links in this server application is like the posts made by the users. All operations depends on authorization.

### Create

The code you need to create a link is:

```
mutation {
  createLink(
    url:"https://www.howtographql.com/graphql-python/0-introduction/",
    description:"This very tutorial"
  ){
    id
    url
    description
  }
}
```

and the answer will be something like this:

```
{
  "data": {
    "createLink": {
      "id": 9,
      "url": "https://www.howtographql.com/graphql-python/0-introduction/",
      "description": "This very tutorial"
    }
  }
}
```

### Query /  Check links

This is how you get the links posted on the server. The code to get them all is:

```
query {
  links {
    id
    url
    description
  }
}
```

and a typical answer can be:

```
{
  "data": {
    "links": [
      {
        "id": "1",
        "url": "https://www.howtographql.com/",
        "description": "The Fullstack Tutorial for GraphQL"
      },
      {
        "id": "3",
        "url": "https://github.com/BrunoOmoreshi",
        "description": "Brunos Github"
      },
      {
        "id": "8",
        "url": "https://www.howtographql.com/",
        "description": "Learn more on GraphQL"
      },
      {
        "id": "9",
        "url": "https://www.howtographql.com/graphql-python/0-introduction/",
        "description": "This very tutorial"
      }
    ]
  }
}
```

### Delete Links

To delete links use something as:

```
mutation {
  deleteLink (id:"9"){
    Link
  }
}
```

### Update Links

To update a link:

```
mutation {
  upDateLink (id:8, description: "Learn more on GraphQL") 
  {
    ok
    }
  }
```

If the id of the link you are trying to change does not exist you may receive the above answer, so please use the check links to query what can be a valid try.

```
{
  "errors": [
    {
      "message": "The link yor are looking for may not exist!",
      "locations": [
        {
          "line": 2,
          "column": 3
        }
      ],
      "path": [
        "upDateLink"
      ]
    }
  ],
  "data": {
    "upDateLink": null
  }
}
```

### Relay

GraphQL has also the possibility to create end points. This is called relay.

You can call this function using:

```
mutation {
  relayCreateLink (input: {
    url: "https://www.howtographql.com/",
    description: "Learn more on GQL"}
  ) {
    link {
      id
      url
      description
    }
  }
}
```

Which means you will create a link with a relay.

The specific answer for the example code is:

```
{
  "data": {
    "relayCreateLink": {
      "link": {
        "id": "TGlua05vZGU6OA==",
        "url": "https://www.howtographql.com/",
        "description": "Learn more on GQL"
      }
    }
  }
}
```

