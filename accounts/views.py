from django.shortcuts import render, get_object_or_404,redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from shopping_cart.models import Order
from django.urls import reverse
from .models import Profile
from products.models import Balance

def register(request):
    if request.method == 'POST':
        #Get form fields
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        #Check passwords
        if password == password2:
            #check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username Is Taken')
                return redirect(reverse('accounts:register'))
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email Already in Use')
                    return redirect(reverse('accounts:register'))
                else:
                    #Great! proceed to register
                    # balance=0
                   
                    user = User.objects.create_user(username=username, password=password, email=email, last_name=last_name, first_name=first_name)
                    # user.save()
                    # Balance(request.user.i,balance).save()

                   
                    # To auto redirect user to dashB
                    # auth.login(request, user)
                    # messages.success(request, 'Await Login...')
                    # return redirect('index')

                    user.save()
                    messages.success(request, 'Registration Successful. Login ')
                    return redirect(reverse('accounts:login'))
        else:
            messages.error(request, 'Passwords do not match')
            return redirect(reverse('accounts:register'))
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Login Successful')
            return redirect(reverse('products:product-list'))
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect(reverse('accounts:login'))
    else:
        return render(request, 'accounts/login.html')

def my_profile(request):
	my_user_profile = Profile.objects.filter(user=request.user).first()
	my_orders = Order.objects.filter(is_ordered=True, owner=my_user_profile)
	context = {
		'my_orders': my_orders,
	}

	return render(request, "profile.html", context)

	
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Logout Success')
        return redirect(reverse('accounts:login'))






