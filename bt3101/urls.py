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
    url(r'^$', login, name='index'),
    url(r'^login', login, name="login"),
    url(r'^forgot-password', forgotPwd),

    url(r'^addresearcher/(?P<queueID>[0-9]+)/$', addResearcher),
    url(r'^addresearcher/(?P<queueID>[0-9]+)/searchresult',searchResult),
    url(r'^researcher/(?P<queueID>[0-9]+)/detail/(?P<persNo>[0-9]+)/$', officerResearcherProfile),

    # for researchers
    url(r'zhanglei', researcherVerify),
    url(r'^changes', researcherChanges),
    url(r'^verified', researcherVerified)
]
