from django.shortcuts import render


def django(request):
    return render(request,'django.html')