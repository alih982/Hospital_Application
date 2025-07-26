from django.shortcuts import render

def renderr(request, name, data=None):
    if data is None:
        data = {}
    return render(request, name + '.html', data)