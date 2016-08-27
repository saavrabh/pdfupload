from django.shortcuts import render
from django.http import HttpResponse

import models
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def get_files(request,proj_id):
	return 1

def add_files(request,proj_id):
	