from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:package>', views.show_package_details, name='package-details')
]