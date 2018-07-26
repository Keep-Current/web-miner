from django.conf.urls import include, url
from django.urls import path

# from django.contrib import admin
# admin.autodiscover()

from . import views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r"^$", views.arxiv, name="index"),
    # url(r'^db', hello.views.db, name='db'),
    #    path('admin/', admin.site.urls),
]
