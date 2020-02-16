from django.shortcuts import render
import re, random


def get_packages():
    packages = {}
    latset_header = None

    with open("app/packages/status.real.txt", encoding="UTF-8") as f:
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

    packages[latset_header] = sorted(packages[latset_header])

    return packages


def index(request):
    context = {'items': get_packages()}
    return render(request, 'packages_index.html', context)


def show_package_details(request, package):
    context = {'item': get_packages().get(package)}
    return render(request, 'packages_details.html', context)
