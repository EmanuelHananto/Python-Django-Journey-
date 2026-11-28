from django.urls import path
from . import views

"""
urlpatterns = [
    path("january/", views.january),
    path("february/", views.february)
]
Top of this are URLconf
"""

urlpatterns = [
    path("", views.index,name="index"),
    path("<int:month>", views.monthly_challenge_int),
    path("<str:month>", views.monthly_challenge, name="monthly_challenge")
]