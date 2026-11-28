from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_blogs, name='all.blogs'),
    path("<slug:slug>/", views.blog_detail, name="blog.detail"),
]
