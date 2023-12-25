


from django.urls import path , include
from django.http import HttpResponse

def index(request):
    return HttpResponse('message', 'message')


urlpatterns = [
    path('',index)
]