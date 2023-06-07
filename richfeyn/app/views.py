from django.shortcuts import render
from .models import signup
# Create your views here.
def home(request):
    return render(request,'home.html')
def privacy(request):
    return render(request,'privacy.html')
# def form(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         saved = signup(email = email)
#         saved.save()
#         return render(request, 'form.html')
def formview(request):
    return render(request , 'form.html')
def form(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        # city = request.POST['city']
        phone = request.POST['phone']
        comment = request.POST['comment']
        pin = request.POST['pin']
        address = request.POST['address']
        newdata = signup(name = name , email = email , phone = phone , comment = comment , pin =pin , address = address)
        newdata.save()
        return render (request, 'home.html')


def main(request):
    return render (request , 'main.html')

def comingsoon(request):
    return render(request , 'coming_soon.html')

def predemo(request):
    return render(request , 'predemo.html')
# def formsub(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         newdata = signup(name = name)
#         newdata.save()
#         return render (request, 'form.html')

# fetch the data from the user


    