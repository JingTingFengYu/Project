from django.http import HttpResponse
from django.shortcuts import render


def cal_view(request):

    return render(request,'cal.html')