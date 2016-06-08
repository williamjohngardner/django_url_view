"""django_views URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from views.views import start_view
from views.views import turtles
from views.views import more_turtles
from views.views import turtle_facts
from views.views import truth
from views.views import realtruth





urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', start_view),
    url(r'^turtles$', turtles),
    url(r'^turtles/moreturtles$', more_turtles),
    url(r'^turtles/moreturtles/turtlefacts$', turtle_facts),
    url(r'^turtles/moreturtles/turtlefacts/thetruth$', truth),
    url(r'^turtles/moreturtles/turtlefacts/thetruth/therealtruth$', realtruth)
]
