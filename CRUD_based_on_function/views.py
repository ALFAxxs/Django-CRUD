from django.shortcuts import render, redirect, get_object_or_404
from CRUD_based_on_forms.models import Orders


def OrderAddView(request):
    if request.method in ['POST', 'FILES']:
        obj = Orders.objects.create(
        image=request.FILES.get('image'),
        video=request.FILES.get('video'),
        fname=request.POST.get('fname'),
        lname=request.POST.get('lname'),
        price=request.POST.get('price'),
        mail=request.POST.get('mail'),
        addr=request.POST.get('addr')
        )
        obj.save()
        return redirect('func:show_orders')
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
            return redirect('func:show_orders')
        else:
            return redirect('func:show_orders')
    template_name = 'crud_func/confirmation2.html'
    context = {
        'obj': obj
    }
    return render(request, template_name, context)


def UpdateOrderView(request, id):
    # Fetch the instance of the order
    order = get_object_or_404(Orders, id=id)

    if request.method == 'POST':
        # Update the instance with new data
        order.image = request.FILES.get('image') if request.FILES.get('image') else order.image
        order.video = request.FILES.get('video') if request.FILES.get('video') else order.video
        order.fname = request.POST.get('fname', order.fname)
        order.lname = request.POST.get('lname', order.lname)
        order.price = request.POST.get('price', order.price)
        order.mail = request.POST.get('mail', order.mail)
        order.addr = request.POST.get('addr', order.addr)

        # Save the updated instance
        order.save()
        return redirect('show_orders')  # Redirect after successful update

    # Prepopulate the data in the template
    template_name = 'crud_func/update_order.html'
    context = {'order': order}
    return render(request, template_name, context)
# def UpdateOrderView(request, id):
#     obj = get_object_or_404(Orders, id=id)
#     template_name = 'crud_func/Orders.html'
#     return render(request, template_name)