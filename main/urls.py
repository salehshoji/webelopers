from django.conf.urls import url
from . import views

urlpatterns = [
    url('signup/',
        views.signup_page_view,
        name='signup-page'),
    url('login/', views.login_page_view, name="login-page"),
    url('logout/', views.logout_page_view, name="logout-page"),
    url('contact_us/', views.contact_us_page_view, name= 'contact-us'),
    url('', views.home_page_view, name='home'),
]
