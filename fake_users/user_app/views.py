from django.shortcuts import render
from user_app.models import User
from user_app import forms

def index(request):
    return render(request, 'user_app/index.html')

def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users': user_list}
    return render(request, 'user_app/users.html', context = user_dict)


# for forms
def form_name(request):
    form = forms.FormName()    
    return render(request, 'user_app/form.html', {'form': form})
