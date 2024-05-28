from django.shortcuts import render
from myapp1.models import Client, Specialist, Service


# Create your views here.
def index_page(request):
    return render(request, 'index.html')

def about_page(request):
    all_client = Client.objects.all()
    return render(request, 'about.html', context={'data3': all_client})

def staff_page(request):
    all_Specialist = Specialist.objects.all()
    return render(request, 'staff.html', context={'data': all_Specialist})

def katalog_page(request):
    all_Service = Service.objects.all()
    return render(request, 'katalog.html', context={'data2': all_Service})