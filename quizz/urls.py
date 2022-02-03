from django.urls import path 
from . import views 
urlpatterns = [
    path("",views.index ,name = "index"),
    path("quiz/",views.main_page, name = "main"),
    path("result/",views.result,name="result")

]