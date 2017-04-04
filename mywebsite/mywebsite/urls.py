#    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')

from django.conf.urls import url, include
from django.contrib import admin

import shop.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^shop/', include('shop.urls')),
    url(r'^account/', include('account.urls')),
    url(r'^$', shop.views.homepage),
]
