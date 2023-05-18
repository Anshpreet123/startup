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
        city = request.POST['city']
        phone = request.POST['phone']
        comment = request.POST['comment']
        newdata = signup(name = name , email = email , city = city , phone = phone , comment = comment )
        newdata.save()
        return render (request, 'form.html')

# def formsub(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         newdata = signup(name = name)
#         newdata.save()
#         return render (request, 'form.html')

# fetch the data from the user


    