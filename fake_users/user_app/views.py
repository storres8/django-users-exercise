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

    if request.method == "POST":
        # allows you to access the form data
        form = forms.FormName(request.POST)
        # if the form is valid run this code which prints what your wrote into terminal
        if form.is_valid():
            print("Form submited!")
            print(f"Name: {form.cleaned_data['name']}")
            print(f"Email: {form.cleaned_data['email']}")
            print(f"Text: {form.cleaned_data['text']}")

    return render(request, 'user_app/form.html', {'form': form})
