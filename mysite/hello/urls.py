from django.urls import path

from . import views

app_name = 'hello'
urlpatterns = [
    # This view will set the cookie and implement the session
    path('', views.index, name='index'),
]

