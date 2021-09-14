![header](D:\Programation\graphql\server_python\header.png)

# Introduction

This project is the result of following the oficial tutorial for a server for backend clone of a blog caled "Hacker News".

The link of tutorial is: https://www.howtographql.com/graphql-python/0-introduction/ 

To accomplish this we are using python as programming language, Django as web frame work. Ok, till here nothing new. But instead off creating a REST application we are creating a GraphQL application. Pretty cool hã?

But what is GraphQL? Ok, is a fair question. But no one is best to answer than the site where I've been using to follow this very tutorial. As they define GraphQL is a new API standard, alternative to REST and developed by Facebook. Ok, but why? Well I can't by other developers, but for me GraphQL have two main strenghs:

- Flexible end points: In a REST application we have for example a end point called ID and it returns certain data. Ok, this sounds obvious, but... Some times servers are desined for a front end or mobile app and some time after things change. Maybe in the mobile app the fields required are diferent from the web app. But we have only one server. Well one may spend a lot of time defining specific end point for each app. Or may create one end point that gives the information needed by the most demmanding app. The problems here are: to spend a lot of time or to send unncessary data to some apps. This is not the case in GraphQL, since  you only receive what you asked for. To do so one need to set in the JSON request what info you may whant to receive.
- Speed to pivot solutions: Since we have a flexible way to retrieve info from a server of ours, we can develop, deliver and deploy features one by one as they are mature enough. Also, there is a "contract" that defines the features that will be available in the very beggining. This means that both teams already knows what and how to implement features for both back end and front end.

## Tips

Also here, I've used some piece of software to play with in the development. For codding I used pyCharm and VS Code. Changed to VS Code because there is Thunder Client extension to be used to connect to our server and use advanced features. On tutorial they reccommend Insomnia, so by the name of curiosity I have made use of it too. Pretty cool, since I don't know a equivalent for Thunder Client in pyCharm, my bad. Some functions worked on browser, so I used the good old fashioned Chrome.

The hard time to jump from one IDE to other is that not all the required packages may needed to be installed again. Even you creating the, very recommneded actualy, Virtual Enviroment, as tutorial say.

Below we can see some prints as "Proof of work" and the code is all available here in this repository.

Some notes for noobs:

In the beggining of the project they say to install the needed packages but they define the versions for these packages. Well... I don't specified and all worked well.

```bash
pip install django graphene-django django-filter django-graphql-jwt
django-admin startproject hackernews
cd hackernews
python manage.py migrate
python manage.py runserver
```

Also, if you never used django you may have a hard time to understand where to create the "links" app. The tip is: on yors IDE open a new terminal navigate to root folder and there execute the command to create. Dont create it by add folder and file by hand.

I had quite a hard time because I had made it and needed to undo, so was needed to change the name of package to "lincks" wich also give me some problems, but also some clarity in how the things worked since wasnt a copy-and-paste task.

```bash
cd hackernews
```

```bash
python manage.py startapp lincks
```

Every time we change the data base schema we must to apply this to the DB instance. To do so:

```python
python manage.py makemigrations

python manage.py migrate
```

Don't forget to be sure that you are in the root directory of the project:

```
cd /hackernews
```

And finnaly one dont need to do all the tutorial in once. You may rest at some point, its ok. But if you are a novice in the development remember that all the times you close your IDE the Django server dies - may it rest in peace. No worry! You can resurrect it! (AMÉN!) To do so, 

```
cd hackernews
```

and start the server:

```
python manage.py runserver
```

## Some pictures

![thunderclient](D:\Programation\graphql\server_python\thunderclient.png)

Here we can see Thunder Client in action, on VS Code. This picture shows the creation of a link with a URL, some description and also the information about the person who made the post - in this case, me. Its needed to open the tab "Headers" and add "AUTHORIZATION" and JWT and the user token, as one can see in the tutorial page.

![pyCharm_server](D:\Programation\graphql\server_python\pyCharm_server.png)

This picture shows the server running on pyCharm. Note that I needed to change the project settings to make some imports work. Thats the reason of the orange folder on the project.

![browser](D:\Programation\graphql\server_python\browser.png)

Now we see the embeded playground of GraphQL that works on browser. Why not follow all the project using this. Wel the thing is that our project uses a moder login method, by tokens, wich unfortunately is not suported by the browser version directly.
