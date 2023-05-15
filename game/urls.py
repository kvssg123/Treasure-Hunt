from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("logincheck/",views.logincheck,name="logincheck"),
    path("logincheck/register/",views.register,name="register"),
    path("<str:id>/level1",views.level1,name="level1"),
    path("<str:id>/level1gift",views.level1gift,name="level1gift"),
    path("<str:id>/level2",views.level2,name="level2"),
    path("<str:id>/level2gift",views.level2gift,name="level2gift"),
    path("<str:id>/level3",views.level3,name="level3"),
    path("<str:id>/level3gift",views.level3gift,name="level3gift"),
    path("<str:id>/level4",views.level4,name="level4"),
    path("<str:id>/level4gift",views.level4gift,name="level4gift"),
    path("<str:id>/level5",views.level5,name="level5")

]   