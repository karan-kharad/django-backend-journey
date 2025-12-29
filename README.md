# FoodeMedia
    "this socal site for share the foodle image with recipes and its like readit,pintrest,intsatgarm"

My Goal is to learn the backend in django 

# Django Project File Structure 

1. __init__.py:
    This file basical empty tell that the this folder is part of the django project

2. asgi.py :
    (Asynchronous Server Gateway Interface.)  this help as to websocket and chat app notification
    working : this hnadle the Asynchronous request
              support the djnago channels

3. setting.py :
    in this filee handle all configuration 
    ex :

    Installed apps
    Database
    Middleware
    Templates
    Static & media files

4. urls.py :
    In this we handle the all routing of url_maping 

5. wsgi.py :
    WSGI is a standard that connects a Python web application to a web server.
    Used for deployment (Gunicorn, uWSGI) Sync servers
    Why WSGI Exists (Truth)
        Python apps (Django, Flask) cannot directly talk to web servers like Nginx or Apache.
        WSGI acts as a bridge between them.


# App File Structure

1. __init__.py:
    This file basical empty tell that the this folder is part of the django project

2. admin.py:
    This control the Admin panel
    what it's work:
    rigister the model 
    enable the CURD in admin UI

3. apps.py:
    App confi it tell the Django what's you app is and how it behave when it loaded 
    what it's work:
    Register the App with Django (its done automaticaly)
    it control the startup bheavoir

4. models.py:
    this handel all DataBase schema that control database 
    what it does:
                1.define the table as class 
                2.Djano ORM convrt the classes -> SQL

5. view.py:
    we write the all logic in this file handle the resonses

    what it's work:
                    1.Receives request
                               |
                    2.process data
                                |
                    3.Return respones

6. urls.py (App level):
    App-specific routing
    Working:
    Included in project urls.py
    Keeps code modular

7. test.py:
    this file automated the testing 

    it help in:
            unite testing 
            integratin testing 
    
8.migrations/
    this floder keep the database version records and migration records 
    it's track the scheme

## mean file 
1. manage.py:
        this file mean use for the command line  control center 

        what it does :
                1. start the develpemt server 
                2.runs migrations 
                3.create superuser
                4.create apps 

2. Templates & static files 
    template :
    *this file content the html css file 
    static:
    *frontend assets


## features
- User Authentication
    Sign up / Login
    Email or phone verification
    Password reset
- User Profile
    Profile photo, bio, username
    Followers / Following count
    Edit profile
- Post Creation
    Text posts
    Image / video upload
    Captions, hashtags
- Feed / Timeline
    Posts from followed users
    Latest or algorithm-based feed
- Like / Reaction System
    Like, heart, etc.
    Real-time count updates
- Comments
    Comment on posts
    Reply to comments
- Follow / Unfollow
    Public & private accounts
    Follow requests (optional)

## Technologies Used
- Python
- Django
- SQLite, PostgrSQL
- HTML, CSS, Bootstrap

## Installation
- djnago
- BeautifulSoup :this package use for webcarkar
- requests :  this for the rquests for anther urls 





## Author
- Name: Karan
- GitHub: https://github.com/karan-kharad


## Web Crawler in Python
In Python, a web crawler is a script/program that:
Sends HTTP requests to websites
Downloads HTML pages
Extracts links and data
Automatically visits new pages
for this we use the BeautifulSoup

