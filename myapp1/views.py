from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_list_or_404, reverse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from myapp1.forms import OrderItemForm, InterestedForm
from myapp1.models import Type, Item, OrderItems


def index(request):
    type_list = Type.objects.all().order_by('id')[:7]
    return render(request, 'myapp1/index0.html', {'type_list': type_list})


def about(request):
    context = {
        'message': 'This is an Online Grocery Store.'
    }
    return render(request, 'myapp1/about0.html', context)


def details(request, type_no):
    types = get_list_or_404(Item, type=type_no)
    return render(request, 'myapp1/details0.html', {'types': types})


def items(request):
    itemlist = Item.objects.all().order_by('id')[:20]
    return render(request, 'myapp1/items.html', {'itemlist': itemlist})

def placeorder(request):
    msg = ''
    itemlist = Item.objects.all()
    if request.method == 'POST':
        form = OrderItemForm(request.POST)
        if form.is_valid():
            item_name = form.cleaned_data['items']
            order = form.save(commit=False)
            if order.number_of_items <= order.items.stock:
                order.save()
                item = Item.objects.get(name=item_name)
                item.stock = item.stock - order.number_of_items
                item.save()
                msg = 'Your order has been placed successfully.'
                return render(request, 'myapp1/order_response.html', {'msg': msg})
        else:
            msg = 'We do not have sufficient stock to fill your order.'
            return render(request, 'myapp1/order_response.html', {'msg': msg})
    else:
        form = OrderItemForm()
    return render(request, 'myapp1/placeorder.html', {'form': form, 'msg': msg, 'itemlist': itemlist})


def order_response(request):
    return render(request, 'myapp1/order_response.html')


def itemdetail(request, item_id):
    itemdetail = Item.objects.get(pk=item_id)
    if request.method == 'POST':
        form = InterestedForm(request.POST)
        if form.is_valid():
            itemdetail.interested = itemdetail.interested + int(form.cleaned_data['quantity'])
            itemdetail.save()
            msg = 'Your interest is added successfully.'
        else:
            msg = 'Sorry for inconvenience! Try again.'
            return render(request, 'myapp1/item_detail.html', {'msg': msg})
    else:
        form = InterestedForm()
    return render(request, 'myapp1/item_detail.html', {'itemdetail': itemdetail, 'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('myapp1:index'))
            else:
                return HttpResponse('Your account is disabled.')
        else:
            return HttpResponse('Invalid login details.')
    else:
        return render(request, 'registration/login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('myapp1:index'))

@login_required
def myorders(request):
    if request.user.is_authenticated:
        orders = OrderItems.objects.filter(client= request.user.pk)
        return render(request, 'myapp1/myorders.html', {'orders': orders})
    else:
        return render(request, 'myapp1/myorders.html', {'msg': 'You are not a registered client!'})

