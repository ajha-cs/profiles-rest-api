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
15. Enabel django-admin for our user profile model (by deafult on for all new projects) -> need to register for new models -> to use django-admin for our user profile model -> go to admin .py (auto created while new app is created)
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
    17.2. ViewSet 