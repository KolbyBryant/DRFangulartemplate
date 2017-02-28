from django.conf.urls import include, url
from django.contrib import admin
from tastypie import Api
from diveshops.views import view_diveshops
from diveshops.api import AjaxSearchResource

rest_api = Api(api_name='v1')
rest_api.register(AjaxSearchResource())

urlpatterns = [
    # Examples:

    url(r'^/?', include('jsframework.urls')),
    url(r'^view_diveshops/(?P<id>\w+)$', view_diveshops, name="view_diveshops"),
    url(r'^view_diveshops/$', view_diveshops, name="view_diveshops")
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(rest_api.urls)),
]
