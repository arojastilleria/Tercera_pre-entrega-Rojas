from django.http import HttpRequest

def saludo(request):
    return HttpRequest("Hola Django - Coder")

def segunda_vista(request):
    return HttpRequest("<br><br> ya esta ok, no es tan simple :")