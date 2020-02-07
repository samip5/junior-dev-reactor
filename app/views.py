from django.views import generic
from django.shortcuts import render
from django.template import RequestContext


class HomePage(generic.TemplateView):
    template_name = "home.html"

