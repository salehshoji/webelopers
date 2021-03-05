from django.conf.urls import url
from products import views
urlpatterns = [
   url('new/', views.new_product, name='new-product'),
]
