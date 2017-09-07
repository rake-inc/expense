from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_user, name='user_home'),
    url(r'^add', views.home_add_details, name='add_expense'),
    url(r'^logout', views.auth_logout, name='auth_logout'),
    url(r'^json/', views.get_json, name='get_json')
]
