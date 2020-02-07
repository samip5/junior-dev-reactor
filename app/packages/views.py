from django.shortcuts import render
import re, random


def index(request):
    packages = {}
    latset_header = None

    with open("app/packages/status.real.txt") as f:
        for l in f:
            l = l.strip()
            # if line contains a keyword
            if "Package: " in l:
                latset_header = l.replace("Package: ", "")
                packages[latset_header] = {'name': latset_header}
            elif "Depends: " in l:
                packages[latset_header]['depends'] = l.replace("Depends: ", "")
            elif "Description: " in l:
                packages[latset_header]["description"] = l.replace("Description: ", "")
            elif "Homepage: " in l:
                packages[latset_header]["homepage"] = l.replace("Homepage: ", "")

    context = {}
    context['items'] = packages

    return render(request, 'index.html', context)


def show_package_details(request, package):
    context = {}
    context['item'] = package
    return render(request, 'index.html', context)