from django.shortcuts import render


def abc(request):
    return render(request,'django.html')