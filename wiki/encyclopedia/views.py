from django.shortcuts import render

from . import util
from django.http import HttpResponse 

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page_view(request, title):
    return HttpResponse (f'the title is: {title}')