from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.templatetags.static import static
from contingut import views
from diari import settings

admin.autodiscover()

urlpatterns = i18n_patterns('',
    # Examples:
    # url(r'^$', 'diari.views.home', name='home'),
    # url(r'^diari/', include('diari.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
                    url(r'^admin/', include(admin.site.urls)),
                    url(r'^index/',
                           views.index,
                           name='index'),
                    url(r'^', include('cms.urls')),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

