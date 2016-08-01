from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^get$',views.getRequest,name="getRequest"),
    url(r'^show$',views.show,name="show"),
    url(r'^hello$',views.serverTest,name="server"),
    url(r'^hello1$',views.clientTest,name="client"),
]