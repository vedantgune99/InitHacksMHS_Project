from django.shortcuts import render

# Create your views here.
def login_user(request):
    return render(request, 'login.html')


def logout_user(request):
    pass


def signin_user(request):
    return render(request, 'signin.html')
