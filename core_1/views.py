from django.shortcuts import render
from django.http import HttpResponse
from core.forms import BMIForm
# Create your views here.

#this creates a simple view
#this requires changes in the todos/settings.py and todos/urls.py
def greeting_view(request):
    # This makes the html from the 'greeting.html' appear from the templates folder.
    return render(request, "greeting.html")

def goodbye_view(request):
    return HttpResponse("Goodbye!")

def bmi(request):
    if request.method == "POST":
        form = BMIForm(request.POST)
        if form.is_valid():
             height = form.cleaned_data['height']
             weight = form.cleaned_data['weight']
             bmi = weight / (height * height)
             return render(request, "bmi.html", {"form": form, "bmi": bmi})
    else:
        form = BMIForm()

    render(request, "bmi.html", {"form":form})
