from django.http import HttpResponse


def index(request):
    return HttpResponse("""Yayyyy! This is my first web app""")
