1. Create a python virtual env first
python3 -m venv ~/env
2. Activate the venv
source ~/env/bin/activate
3. Deactivate
deactivate
4. django-admin startproject profiles_project . 
5. python manage.py startapp profiles_api -> creates new django app 
6. enable new app in project
7. settings.py -> INSTALLLED_APPS (either externally or internally) -> profiles_api, rest_framework, rest_framework.authtoken
8. Server start kr diya -> python manage.py runserver 0.0.0.0:8000
0.0.0.0 -> means available to all n/w adaptors of our server
8000 -> port no. -> same in settings.py
http://127.0.0.1/ -> local host address
9. models reqd. to describe data -> django uses this model -> to store our data -> each model in django maps to db
10. Create our user db model -> our own custom model (there is default model)
11. SuperUser -> command in cli to add superuser (admin - full control can see all the models in db)
12. configure django for custom user model -> settings.py -> AUTH_USER_MODEL = 'profiles_api.UserProfile'
13. create django Migration file -> to manage our db -> have steps reqd. to make matches with db and our django model -> create a migration file for our model ->
    13.0. first activate the venv
    13.1. create a migration file -> python manage.py makemigrations profiles_api
    13.2. All steps req. to create our model
    13.3. Run our migration -> python manage.py migrate -> run all migrations -> create
    all required models -> auth system, tables in our db
14. Creating our superuser -> enabling django admin -> tool to create admin website for your project and let us manage (inspect-modify) our db models -> create a superuser -> python mnanage.py createsuperuser
15. Enable django-admin for our user profile model (by default on for all new projects) -> need to register for new models -> to use django-admin for our user profile model -> go to admin .py (auto created while new app is created)
16. 3 sections -> 3 apps -> authtoken app (comes out of djangorest fwmrk) -> authentication and authorization (comes out of django) -> profiles_api app (with the models we define -- we can override this behavior too) 
17. API Views -> dj rest frmwrk offers couple of helper classes to create our api endpoints
    17.1. APIView -> most basic view to build our api -> describe logic to make api endpoints -> apiview (allow us to define the func that matches the standard HTTP method - GET, PUT, POST, PATCH, DELETE) -> allows us to customise the function for each HTTP on api url -> most control ovr the logic -> perfect for implementing the complex logic -> like calling other apis or working with local files -> USE - 
    1. Need full control over logic - complex logic, update multiple data sources in one api call
    2. processing files and rendering a synchronous response
    3. Calling ohther apis and service
    4. Accessing local files or data 
    5. API View is set
    6. Let's wire this up to the url in django -> urls.py in root project directory -> entrypoint for every urls -> admin/ (created by default) -> looks up url and matche s with first url it finds -> admin.site.url -> connects url with admin app 
    7. for our profiles_api -> new urls.py -> import path -> import views -> urlpatterns
    8. Add a **serializer** to the view -> from djrestfmwk allows you to convert data inputs into python object and vice versa - just like django forms 
    9. create new file serializers.py -> import serialisers -> used it while post/update requeest
    10. Add POST method to API View
    11. Test Post function 
    12. PUT, Patch - Raw data in pg, Delete
    13. 
    vs 
    17.2. ViewSet -> Allows us to write logic for endpoints -> insted of defining func which match to http method -> accept func that maps to common api object action -> list, create, retrieve, update, partial_update, destroy -> takes care of common logic for us -> perfect for writing api that performs standard db opn -> fastest way to make api -> USES
    1. A simple CRUD over db
    2. A quick and simple API
    3. Little to no customization on the logic
    4. working with standard database structure
    5. create HelloViewSet class -> import viewsets from restfwk -> done
    6. set url to point our viewset -> different from apiview -> viewsets - it calls a Router class provided by djrestfmwk to generate different routes available for our viewset -> import include from django.urls -> includeing list of url in url_patterns -> import DefaultRouter restfmwk.routers -> then create a object and register the viewset for the same.
    7. serializer class -> same one can be used -> used in post request -> serializer_class -> self.serializer_class -> validate 
    8. add retrieve, update ... func
    9. No put, patch, delete method here on viewset api -> bcoz viewset expect that we'll use this end point to retrieve a list of objects in the db -> we'll specify pk to make changes -> add something after url - for eg: /id:201
18. Create a serializzer for user profile object
19. **model serializzers** -> extra functionality -> import models to aces user profile model -> use a meta class to configure serializer to point our model -> fields - tuple
20. create a view set to access a serializer through end point -> ModelViewSet
21. Register it with url
22. Test this
23. Create Premission Class -> any user can change other profiles -> must be authenticated -> restrict useres -> using dj permisssion class ->  import permissions module from rest fwk -> done
24. Configure viewset to use this permissions -> TokenAuthentication from drf -> for user to authenticate with our api -> genereate a random token string and get added whenever the request is made -> import permissions module
25. Test new permissions
26. Ability to search profiles -> filter -> import filters -> done
27. Test Searching Profiles -> ? - to signify first get parameter **?search=Mark**
28. Adding a Login Functionality -> using TokenAuthnetication -> including tokens in headers while request is made -> add a endpoint to our api that allows you to generate a auth Token -> import ObtainAuthToken -> import apisetttings -> add url to this view to enable it
29. Test Login API -> give token
30. Set Token Header using ModHeader extensions -> every request has HTTP header -> add a authorization key with this token -> when dj recives the request check for this token in db -> we'll be passing token in which ever client library - JS(fetch) we're using
31. User Feed API -> Create a new django model for storing user profile feed items -> import settings.py from django.conf() from profiles_project -> doen
32. run the migrations -> create a table in db -> To reflect changes -> python manage.py migrate
33. Register this in django admin -> done
34. Create a serializer for our profile feed object
35. Create a viewset for our profile feed items
36. Test it
37. Create  a permissions class -> using IsAuthenticatedOrReadOnly