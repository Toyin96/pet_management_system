from django.shortcuts import render
from django.http import Http404
from .models import Pet


# Create your views here.

def home(request):
    pets = Pet.objects.all()

    context = {"pets": pets}
    return render(request, "adoptions/home.html", context)


def pet_detail(request, pet_id):
    try:
        pet = Pet.objects.get(id=pet_id)
    except Pet.DoesNotExist:
        raise Http404("No pet found with that ID")

    return render(request, "adoptions/pet_detail.html", {"pet": pet})
