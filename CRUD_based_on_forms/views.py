from django.shortcuts import render, redirect
from .forms import OrdersForm
from .models import Orders

#Create a Order (Create View) In crudapp/views.py, define a view function for creating a new order
def OrderFormView(request):
    form = OrdersForm()
    if request.method == 'POST':
        form = OrdersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'crudapp/orders.html'
    context = {
        'form': form
    }
    return render(request, template_name, context)


#Read Orders (List View) Now, let's create a view to display a list of all books in crudapp/views.py:
def ShowOrderView(request):
    obj = Orders.objects.all()
    template_name = 'crudapp/show.html'
    context = {
        'obj':obj
    }
    return render(request, template_name, context)


#Update a Order (Update View) To update a order, create a view in crudapp/views.py:
def UpdateOrderView(request):
    obj = Orders.objects.all()
    form = OrdersForm(instance=obj) #instance = obj -> bu yerda oldingi ma'lumotlarni ko'rsatish uchun
    if request.method == POST:
        form = OrdersForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'crudapp/order.html'
    context = {
        'form': form
    }
    return render(request, template_name, context)


#Delete a Order (Delete View) Finally, let's create a view to delete a order in crudapp/views.py:
def DeleteOrderView(request, id):
    obj = Orders.object.get(id=id)
    if request.method == POST:
        obj.delete()
        return redirect('show_url')
    template_name = 'crudapp/confirmation.html'
    context = {
        'obj': obj
    }
    return render(request, template_name, context)