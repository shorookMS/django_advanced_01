from django.shortcuts import render
from .models import Inventory
# Create your views here.

def inventory_list(request):
	inventories = Inventory.objects.all()
	context = {
		'inventories':inventories,
	}
	return render(request,'inventory_list.html',context)
