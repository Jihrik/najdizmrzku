from django.shortcuts import render
from .models import Store

def home(request):
    stores = Store.objects.all()
    
    context = {'stores': stores}
    return render(request, 'najdizmrzkuapp/store_component.html', context)
    