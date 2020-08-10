from django.shortcuts import render

def home_view(req):
    return render(req, 'home.html')
