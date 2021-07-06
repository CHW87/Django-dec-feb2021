from django.shortcuts import render

cars = [
    {"model": 'BMW', "year": 2020},
    {"model": 'Audi', "year": 2010},
    {"model": 'KIA', "year": 2008},
]


# Create your views here.
def home(request):
    return render(request, 'index.html', {"cars": cars})


def add_car(request, year, model):
    cars.append({'model':model, 'year':year})
    return render(request, 'index.html', {"cars": cars})
