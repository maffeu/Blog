from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# @login_required(login_url='login')
def home(request):
    name = 'Klassic mann'
    context= {'name':name, 'age':33, 'address':'Douala'}
    return render(request, 'base.html', context)

def contact(request):
    return render(request, 'contact.html')

def news(request, id):
    ourId = id
    return render(request,  'news.html', {'newId':ourId})