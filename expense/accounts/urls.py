from django.conf.urls import url
from django.urls import reverse
from . import views

urlpatterns = [
    url(r'^$', views.profile, name='profile'),
    url(r'^add_category/', views.add_category)
]
