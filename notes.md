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
