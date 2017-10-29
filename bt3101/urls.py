"""bt3101 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
        /
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
from capstone.views import *

urlpatterns = [
    # for login
    url(r'^$', index, name='index'),
    url(r'^login', login),
    url(r'^forgot-password', forgotPwd),
    url(r'^addresearcher', addResearcher),
    #url(r'^researcher', researcher),
    url(r'^researcher/detail', researcher),
    url(r'^searchedresults', searchedResults),
    url(r'^searchresult',searchResult),

    url(r'^usermain', usermain),

    # for researchers
    url(r'^changes', researcherChanges),
    url(r'^verified', researcherVerified)
]
