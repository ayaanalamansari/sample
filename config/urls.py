"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import include, url
# from django.conf import settings
# from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('region_management.routers'))
]
# urlpatterns = [
#     # Examples:
#     # url(r'^$', 'region_management.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),

#     url(r'^api/v1/', include('region_management.routers', namespace='v1')),
#     # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

#     url(r'^superadmin/', include(admin.site.urls)),
# ]


# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns += [
#         url(r'^__debug__/', include(debug_toolbar.urls)),
#     ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
