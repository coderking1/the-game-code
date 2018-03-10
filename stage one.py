from django.http import HttpResponse


def index(request):
    return HttpResponse("the destroyer of worlds -- aggoretath -- hath come once more!")
