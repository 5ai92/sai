from django.conf.urls import include, url, patterns
from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')), 
    url(r'^admin/', include(admin.site.urls)),  
    url(r'^', include('home.urls')),
    url(r'^', include('blog.urls')),
    url(r'^', include('stocks.urls')),
)
