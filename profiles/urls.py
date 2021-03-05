from django.conf.urls import url
from profiles import views
urlpatterns = [
   url('', views.profile, name='profile-page')
]
