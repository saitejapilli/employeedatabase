from django.http import HttpResponse
def home(request):
    return HttpResponse("python is both object oriented and procedure oriented language")