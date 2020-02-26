from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.HomePage.as_view(), name="home"),
    path("package/", include('app.packages.urls')),
    path("admin/", admin.site.urls)
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns.append(path("__debug__/", include(debug_toolbar.urls)))
