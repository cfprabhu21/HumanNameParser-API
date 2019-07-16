from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = {
    url(r'^humannameparser/$', views.GetHumanNameParser.as_view()),
}

urlpatterns = format_suffix_patterns(urlpatterns)
