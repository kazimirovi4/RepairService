from django.shortcuts import render

from repair.models import Service


def service_list(request):
    services = Service.objects.all()
    return render(request, 'repair/index.html', {'services':services})