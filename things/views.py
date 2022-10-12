from django.shortcuts import render
from things import forms

def home(request):
    form = forms.ThingForm()
    return render(request, 'home.html', {'form': form})
