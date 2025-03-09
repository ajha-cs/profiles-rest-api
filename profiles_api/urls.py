from django.urls import path

from profiles_api import views

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    #as_view() -> convert api view class to be rendered by url
]