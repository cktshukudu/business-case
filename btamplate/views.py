
from django.http import HttpResponse
from django.shortcuts import render


def index(response):
    return render(response, "btamplate/base.html", {})

def main(response):
    return render(response, "btamplate/main.html", {})