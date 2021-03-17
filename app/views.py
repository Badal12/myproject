from django.shortcuts import render
from django.views import View
from . models import Customer, Product, Cart, OrderPlaced
from . forms import CustomerRegistrationForm  #will import the form for userregistration
from django.contrib import messages

'''here we are rendering the home.html and we are gone write the 
logic of filtering the bottom-wear product, mobile product, etc and we are gonna pass 
it using for loop inside the home.html
'''
#def home(request):
# return render(request, 'app/home.html')
#-we are gona create the class base view of home.html--Product view
'''
on the base on category we are gonna filter it from db of models created field
filter the product according to category and put into perticular field
'''
class ProductView(View):
 def get(self, request):
  topwears = Product.objects.filter(category='TW')
  bottomwears = Product.objects.filter(category='BW')
  mobiles = Product.objects.filter(category='M')
  return render(request, 'app/home.html', {'topwears': topwears, 'bottomwears': bottomwears, 'mobiles': mobiles})
#now we will pass this filter thorough context through dictionaryin the home.html file can print using for loop
'''
when we click on any product we should get all the details with unique id of product
for that we will have to write the class base view and same as have to pass the that to html file
'''

class ProductDetailView(View):
 def get(self, request, pk):
  product = Product.objects.get(pk=pk) #from db will fetch the id and assign to it
  return render(request, 'app/productdetail.html', {'product': product}) #here we have to change the .html

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')


def mobile(request, data=None): #when this data will come then only below logic will work.how can we pass that data
 #basically we can pass the data by url
 if data == None: #None means data nhi aa raha hai
  mobiles = Product.objects.filter(category='M') #then it will filter all mobiles category
 elif data == 'Redmi' or data == 'Samsung':
  mobiles = Product.objects.filter(category='M').filter(brand=data)
 elif data == 'below':
  mobiles = Product.objects.filter(category='M').filter(discounted_price__lt=10000)
 elif data == 'above':
  mobiles = Product.objects.filter(category='M').filter(discounted_price__gt=10000)

 return render(request, 'app/mobile.html', {'mobiles': mobiles})

#we are gonna use a django-builtin authontication module for login
#we dont nedd to write the view
#def login(request):
# return render(request, 'app/login.html')

#def customerregistration(request):
# return render(request, 'app/customerregistration.html')
#we will create a class base form
class CustomerRegistrationView(View):
 def get(self, request):
  form = CustomerRegistrationForm()
  return render(request, 'app/customerregistration.html', {'form': form})
 #if form comes with data then post() will called
 def post(self, request):
  form = CustomerRegistrationForm(request.POST)
  if form.is_valid():
   messages.success(request, 'congratulations!! Registered Successfully ')
   form.save()
  return render(request, 'app/customerregistration.html', {'form': form})

def checkout(request):
 return render(request, 'app/checkout.html')
