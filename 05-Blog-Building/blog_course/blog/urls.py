from django.urls import path
from . import views

urlpatterns = [
    path("", views.mainpage, name="mainpage"),
    path("posts", views.posts,name="posts"),  
    path("posts/<slug:slug>",views.postlists,
         name="postlist" )
]