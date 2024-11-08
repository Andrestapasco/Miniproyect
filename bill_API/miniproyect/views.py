from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Item

# Create your views here.
#get


def item_list(request):
    items = Item.objects.all().values() 
    return HttpResponse(list(items))






# def item_list(request):
#     items = Item.objects.all()
#     return render(request, 'Mini/item_list.html', {'items': items})



#post
@csrf_exempt
def item_create(request):
    if request.method == 'POST':
        data = json.loads(request.body) 
        name = data.get('name')
        description = data.get('description')
        new_item = Item.objects.create(name=name, description=description)
        
        
        return JsonResponse({# devuelve el nuevo ítem en tipo json
            'id': new_item.id,
            'name': new_item.name,
            'description': new_item.description
        })
    return JsonResponse({'error': 'POST request required'}, status=400)




# def item_create(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         description = request.POST.get('description')
#         Item.objects.create(name=name, description=description)
#         return redirect('item_list')
#     return render(request, 'Mini/item_create.html')