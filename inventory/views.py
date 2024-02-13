from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import ReceiverForm
from inventory.models import Supplier, Product, Receiver
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import F, Prefetch
import datetime

# Create your views here.
def login_view(request):
    # handle login form submission
    if form.is_valid():
        login(request, user)
        return redirect('inventory:index')
    # return login form
    return render(request, 'registration/login.html')

def index(request):
    products = Product.objects.all()
    all_prods = len(Product.objects.all())
    total_products = all_prods
    context = {
        'title': 'Home',
        'products': products,
        'count_products': all_prods,
        'total_products': total_products,
    }
    return render (request,"index.html")

def add_supplier(request):
    if request.method == 'POST':
        supplier_id = request.POST['supplierid']
        supplier_name = request.POST['suppliername']
        supplier_email = request.POST['supplieremail']
        supplier_phonenum = request.POST['supplierphonenum']
        supplier_address = request.POST['supplieraddress']
        data = Supplier(supplierid=supplier_id, suppliername=supplier_name, supplieremail=supplier_email, supplierphonenum=supplier_phonenum, supplieraddress=supplier_address)
        data.save()
        dict = {
            'message':'Supplier successfully added'
        }
    else:
        dict = {
            'message':''
        }
    return render(request, "add_supplier.html", dict)

def supplier(request):
    allsupplier = Supplier.objects.all()
    dict = {
        'allsupplier':allsupplier
    }
    return render(request, "supplier.html", dict)

def edit_supplier(request,supplierid):
    data = Supplier.objects.get(supplierid=supplierid)
    dict = {
        'data':data
    }
    return render(request, "edit_supplier.html", dict)

def save_edit_supplier(request, supplierid):
    sp_name = request.POST['suppliername']
    sp_email = request.POST['supplieremail']
    sp_phonenum = request.POST['supplierphonenum']
    sp_address = request.POST['supplieraddress']
    data = Supplier.objects.get(supplierid=supplierid)
    data.suppliername = sp_name
    data.supplierphonenum = sp_phonenum
    data.supplieremail = sp_email
    data.supplieraddress = sp_address
    data.save()
    return HttpResponseRedirect(reverse("supplier"))

def delete_supplier(request, supplierid):
    data = Supplier.objects.get(supplierid=supplierid)
    data.delete()
    return HttpResponseRedirect(reverse("supplier"))

def add_product(request):
    if request.method == 'POST':
        product_id = request.POST['productid']
        product_name = request.POST['productname']
        suppliername = request.POST['supplier']
        product_qty = request.POST['productqty']
        product_price = request.POST['productprice']

        # retrieve the supplier instance using the suppliername
        supplier = Supplier.objects.filter(suppliername=suppliername).first()

        if not supplier:
            dict = {
                'message': 'No supplier with such suppliername found'
            }
            return render(request, "add_product.html", dict)

        # create a new product instance with the supplier instance
        data = Product(productid=product_id, productname=product_name, supplier=supplier, productqty=product_qty, productprice=product_price)
        data.save()
        dict = {
            'message':'Product successfully added'
        }
    else:
        dict = {
            'message':''
        }
    return render(request, "add_product.html", dict)

def product(request):
    allproduct = Product.objects.all()
    dict = {
        'allproduct':allproduct
    }
    return render(request, "product.html", dict)

def edit_product(request,productid):
    data = Product.objects.get(productid=productid)
    dict = {
        'data':data
    }
    return render(request, "edit_product.html", dict )

def save_edit_product(request, productid):
    p_name = request.POST['productname']
    p_qty = request.POST['productqty']
    p_price = request.POST['productprice']
    data = Product.objects.get(productid=productid)
    data.productname = p_name
    data.productqty = p_qty
    data.productprice = p_price
    data.save()
    return HttpResponseRedirect(reverse("product"))

def delete_product(request,productid):
    data = Product.objects.get(productid=productid)
    data.delete()
    return HttpResponseRedirect(reverse("product"))

def app_form(request):
    if request.method == 'POST':
        receiver_name = request.POST['receivername']
        receiver_positions = request.POST['receiverpositions']
        productname = request.POST['product']
        receive_qty = request.POST['receiveqty']
        receive_date = request.POST['receivedate']

        # retrieve the product instance using the productname
        product = Product.objects.filter(productname=productname).first()

        if not product:
            dict = {
                'message':'No product found'
            }
            return render(request, "app_form.html",dict)

        # create a new inventory instance with the product instance
        data = Receiver(receivername=receiver_name, receiverpositions=receiver_positions, product=product, receiveqty=receive_qty, receivedate=receive_date)
        data.save()
        dict = {
            'message':'Application submitted'
        }
    else:
        dict = {
            'message':''
        }
    return render(request, "app_form.html", dict)

def receiver(request):
    allreceiver = Receiver.objects.all()
    dict = {
        'allreceiver':allreceiver
    }
    return render(request, "receiver.html", dict)

def edit_receiver(request,receiverid):
    data = Receiver.objects.get(receiverid=receiverid)
    dict = {
        'data':data
    }
    return render(request, "edit_receiver.html", dict)

def save_edit_receiver(request, receiverid):
    receive_status = request.POST['receivestatus']
    data = Receiver.objects.get(receiverid=receiverid)
    data.receivestatus = receive_status
    data.save()
    return HttpResponseRedirect(reverse("receiver"))
