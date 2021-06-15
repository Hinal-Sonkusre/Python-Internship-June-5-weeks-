from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def homepageview(request):
    return render(request, 'home.html')


def aboutpageview(request):
    return render(request, 'about.html')


def contactpageview(request):
    return render(request, 'contact.html')


def my_form(request):
    return render(request, 'my_form.html')


def process(request):
    print("Welcome")
    print(request.method)
    print(request.POST)
    a = str(request.POST['fname'])
    print(a)
    b = str(request.POST['mname'])
    print(b)
    c = str(request.POST['lname'])
    print(c)
    d = int(request.POST['number'])
    print(d)
    e = str(request.POST['email'])
    print(e)
    return render(request, 'ans.html', {'mya': a, 'myb': b, 'myc': c, 'myd': d, 'mye': e})
