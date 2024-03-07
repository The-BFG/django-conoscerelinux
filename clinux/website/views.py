from django.shortcuts import render


def index(request):
    context = {
        'message': 'World'
    }
    return render(request, "index.html", context)
