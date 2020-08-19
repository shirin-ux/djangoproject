from django.http import HttpResponse
from django.shortcuts import render


def movie_list(request):
    return HttpResponse('salam')
