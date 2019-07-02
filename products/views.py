from __future__ import unicode_literals
from .models import Product,Balance
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.utils.translation import ugettext_lazy as _
from shopping_cart.models import Transaction, Order
from accounts.models import Profile
from django.urls import reverse


def get_user_pending_order(request):
    # get order for the correct user
    user_profile = get_object_or_404(Profile, user=request.user)
    order = Order.objects.filter(owner=user_profile, is_ordered=False)
    if order.exists():
        # get the only order in the list of filtered orders
        return order[0]
    return 0
    
def product_list(request):
    object_list = Product.objects.all()
    paginator = Paginator(object_list, 5)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    user_profile = get_object_or_404(Profile, user=request.user)
    filtered_orders = Order.objects.filter(owner=user_profile, is_ordered=False)
    current_order_products = []
    if filtered_orders.exists():
        user_order = filtered_orders[0]
        user_order_items = user_order.items.all()
        current_order_products = [product.product for product in user_order_items]
        
    order_to_purchase = get_user_pending_order(request)
    if order_to_purchase == 0:
        amount = 0 
    else:
        amount = order_to_purchase.get_cart_total()
 
    account_bal=Balance.objects.all()
    money_avail=account_bal.filter(user=request.user).last()
    change=(money_avail.balance-amount)
    
    if amount != 0:
        change=(money_avail.balance-amount)
        print(change)
        Balance.objects.filter(id=1,user=request.user).update(balance=change)   
    else:
        change =money_avail.balance
        print("a",amount)
    
    # get user top up
    if request.method == 'POST':
        balances = int(request.POST['balance'])
        balance=balances
        if balances <=0:
            return redirect(reverse('products:product-list'))
        updatez=sum([money_avail.balance,balance])
        user = request.user 
        balances = Balance(balance=updatez,user=user)
        balances.save()
    
    context = {
        'change':change,
        'object_list': paged_listings,
        'current_order_products': current_order_products
    }

    return render(request, "products/product_list.html", context)
