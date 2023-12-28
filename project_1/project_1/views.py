
from django.http import  HttpResponse
def home(request):
    return HttpResponse("this home page")
def contact(request):
    return HttpResponse("This contact page")