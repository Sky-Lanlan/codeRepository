from django.conf.urls import url
from app01 import views as app01views

urlpatterns = [
        url(r'^$',app01views.Home.as_view())
]