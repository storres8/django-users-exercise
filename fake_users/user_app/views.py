from django.shortcuts import render
from user_app.models import User

def index(request):
    return render(request, 'user_app/index.html')

def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users': user_list}
    return render(request, 'user_app/users.html', context = user_dict)
