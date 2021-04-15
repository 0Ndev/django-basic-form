from django.conf.urls import url
from user_form import views

urlpatterns = [
    url(r'^$', views.users, name='users')
]
