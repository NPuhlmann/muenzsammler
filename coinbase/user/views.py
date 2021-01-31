from django.shortcuts import render
from .forms import UserCreateForm


# Create your views here.
def register(response):
    if response.method == 'POST':
        form = UserCreateForm(response.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreateForm()
    return render(response, "registration/register.html", {"form": form})
