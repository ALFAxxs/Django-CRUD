from django.shortcuts import render, redirect, get_object_or_404
from CRUD_based_on_forms.models import Orders


def OrderAddView(request):

    template_name = 'crud_func/Orders.html'
    return render(request, template_name)


def ShowOrderView(request):
    obj = Orders.objects.all()
    context = {
        'obj': obj
    }
    template_name = 'crud_func/show_orders.html'
    return render(request, template_name, context)


def DeleteOrderView(request, id):
    obj = get_object_or_404(Orders, id=id)
    if request.method == 'POST':
        if 'confirm' in request.POST:
            obj.delete()
            return redirect('show_orders')
        else:
            return redirect('show_orders')
    template_name = 'crud_func/confirmation.html'
    context = {
        'obj': obj
    }
    return render(request, template_name, context)