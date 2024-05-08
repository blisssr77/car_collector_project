from django.shortcuts import render, redirect
from .models import Car, Option
from .forms import RentalForm
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

initial_cars = [
    {
        'model': 'Bugatti Chiron Super Sport 300+',
        'year': 2021,
        'horsepower': 1600,
        'msrp': '3.9M',
        'madein': 'France'
    },
    {
        'model': 'Hennessey Venom F5',
        'year': 2017,
        'horsepower': 1817,
        'msrp': '2.1M',
        'madein': 'United States'
    },
    {
        'model': 'SSC Tuatara',
        'year': 2020,
        'horsepower': 1750,
        'msrp': '1.6M',
        'madein': 'United States'
    },
    {
        'model': 'Koenigsegg Jesko',
        'year': 2020,
        'horsepower': 1600,
        'msrp': '3.0M',
        'madein': 'Sweden'
    },
    {
        'model': 'Ferrari SF90 Stradale',
        'year': 2020,
        'horsepower': 1000,
        'msrp': '1.5M',
        'madein': 'Italy'
    },
    {
        'model': 'McLaren P1',
        'year': 2013,
        'horsepower': 903,
        'msrp': '1.1M',
        'madein': 'United Kingdom'
    },
    {
        'model': 'Lamborghini Aventador SVJ',
        'year': 2018,
        'horsepower': 770,
        'msrp': '0.8M',
        'madein': 'Italy'
    },
    {
        'model': 'Porsche 918 Spyder',
        'year': 2013,
        'horsepower': 887,
        'msrp': '0.8M',
        'madein': 'Germany'
    },
    {
        'model': 'Aston Martin Valkyrie',
        'year': 2021,
        'horsepower': 1160,
        'msrp': '3.0M',
        'madein': 'United Kingdom'
    },
    {
        'model': 'Pagani Huayra BC',
        'year': 2016,
        'horsepower': 791,
        'msrp': '2.6M',
        'madein': 'Italy'
    },
]

# Create your views here.
def home(request):
    # return HttpResponse("hello")
    return render(request, 'cars/home.html')

def about(request):
    return render(request, 'cars/about.html')

def cars_index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', {
        'cars': cars,
    })

def cars_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    options = Option
    id_list = car.options.all().values_list('id')
    print(id_list)
    options_car_doesnt_have = Option.objects.exclude(id__in=id_list)
    rental_form = RentalForm()
    return render(request, 'cars/detail.html', { 
        'car': car, 'rental_form': rental_form,
        'options': options_car_doesnt_have
        })

def assoc_option(request, pk, option_pk):
    Car.objects.get(id=pk).options.add(option_pk)
    return redirect('detail', car_id=pk)

def assoc_delete(reuqest, pk, option_pk):
    Car.objects.get(id=pk).options.remove(option_pk)
    return redirect('detail', car_id=pk)

    
class CarCreate(CreateView):
    model = Car
    fields = ['model', 'madein', 'year', 'msrp', 'horsepower', 'image']

class CarUpdate(UpdateView):
    model = Car
    fields = ['model', 'madein', 'year', 'msrp', 'horsepower', 'image']

class CarDelete(DeleteView):
    model = Car
    success_url = '/cars/'

def add_rental(request, pk):
    form = RentalForm(request.POST)
    if form.is_valid():
        new_rental = form.save(commit=False)
        new_rental.car_id = pk
        new_rental.save()
    return redirect('detail', car_id=pk)

class OptionList(ListView):
    model = Option

class OptionDetail(DetailView):
    model = Option

class OptionCreate(CreateView):
    model = Option
    fields = '__all__'

class OptionUpdate(UpdateView):
    model = Option
    fields = ['name', 'color']

class OptionDelete(DeleteView):
    model = Option
    success_url = '/options'


