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