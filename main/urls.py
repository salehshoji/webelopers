from django.conf.urls import url
from . import views

urlpatterns = [
    url('signup/', views.signup_page_view, name='signup-page'),
    url('', views.home_page_view, name='home'),
]
