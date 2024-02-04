from django.shortcuts import render
# from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, Orderitem, Order, Customer, Promotion
from django.db.models import Q, F, Value, Func, Count, Sum, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from django.db.models import Max, Min, Avg, Count, Sum
from django.contrib.contenttypes.models import ContentType
from tags.models import Tagitem
from django.db import IntegrityError
from store.forms import userform
# Create your views here.


#def home(request):
 #   query_set = Product.objects.all()
  ##  customer_lj = Customer.objects.annotate(
    #order_count=Count('order'),
  #  total_sum=Sum('points')
   # )

    #customer_ij = Customer.objects.filter(order__isnull=False).annotate(
     #   order_count=Count('order'),
      #  total_sum=Sum('points')
    #)
    #return render(request,'index.html',{'cus_lj':customer_lj,'cus_ij':customer_ij})
    
    # objects is manager that is a interface of database
    # for p in query_set:
    #     print(p)
    # product = Product.objects.get(pk=5)
    # print(product)
    # get only specific record using where clause
    # try:
    #     product = Product.objects.get(pk=0)
    # except ObjectDoesNotExist:
    #     pass

    # product = Product.objects.filter(pk=0).exists()
    # Filtering Data
    # find those dollars who have unit_price = 20
    # product = Product.objects.filter(price=20)
    # for p in product:
    #         print(p)

    # Filter using
    # keyword argument
    # query_set api
    # product = Product.objects.filter(price__gte=23.29)
    # for p in product:
    #     print(p)

    # product = Product.objects.filter(title__contains='Wine')
    # product = Product.objects.filter(inventory__lt=10,price__lt=20)
    # product = Product.objects.filter(inventory__lt=10).filter(price__lt=20)
    # Q object to make complex lookups
    # product = Product.objects.filter(Q(inventory__lt=10)& ~Q(price__lt=40))
    # We can compare related fields with F class Object
    # product = Product.objects.filter(inventory=price)
    # Sort in Ascending order
    # Order_by is a quert_set method so its return a query objects
    # product = Product.objects.filter(collection_id=5).order_by('price').reverse()
    # pl = Product.objects.latest('id')
    # pe = Product.objects.earliest('id')
    # product = Product.objects.all()[:5]
    # product = Product.objects.all()[4:10]
    # product = Product.objects.values('id','title','description','price','inventory','collection__title')
    # Tasks Select Products that have been ordered
    # And Sort them by title
    # product = Orderitem.objects.values('product_id__id', 'product_id__title', 'product_id__description',
    #                                    'product_id__price', 'product_id__inventory', 'unit_price').order_by('product_id__title')
    # product = Product.objects.only('id','title','price','description','inventory','last_update')
    # product = Product.objects.only('id','title','description','inventory','last_update')
    # product = Product.objects.all()
    # product = Product.objects.select_related('collection').all()
    # select_related (1)
    # prefetch_related (n)
    # product = Product.objects.prefetch_related('promotions').all()
    # product = Product.objects.select_related('collection').prefetch_related('promotions').all()
    # product = Product.objects.prefetch_related('promotions').all()
    # Task
    # Get the last 5 orders with their customer
    # and items (incl product)
    # order = Order.objects.select_related('customer').prefetch_related(
    #     'orderitem_set__product').order_by('-id')[:5]
    # result = Product.objects.aggregate(count=Count('id'), min_price=Min(
    #     'price'), max_price=Max('price'), average=Avg('price'))

    # result_collection = Product.objects.filter(collection__id=5).aggregate(count=Count('id'), min_price=Min(
    #     'price'), max_price=Max('price'), average=Avg('price'), total_sum=Sum('price'))

    # customer = Customer.objects.annotate(bonus=F(
    #     'points')+30, full_name=Func(F('first_name'), Value(' '), F('last_name'), function='CONCAT'))

    # customer = Customer.objects.annotate(
    #     bonus=F(
    #         'points')+30,
    #     full_name=Concat('first_name', Value(' '), 'last_name'))


    # disc = ExpressionWrapper(F('price')*0.8, output_field=DecimalField())
    # product = Product.objects.annotate(
    #     discounted_price=disc)

    # return render(request, 'index.html', {'product': product, 'result': result, 'order': order, 'result_collection': result_collection, 'customer': customer, 'cus_lj': customer_lj, 'cus_ij': customer_ij})

    # query = Tagitem.objects.get_tags_for(Product,1)
    # promotion = Promotion()
    # promotion.description = "The classes documented below provide a way for users to use functions provided by the underlying database as annotations, aggregations, or filters in Django"
    # promotion.discount = 32.34
    # promotion.featured_product = Product(pk=3)
    # # promotion.featured_product_id=3
    # promotion.save()
    # pro = Promotion.objects.get(pk=26)
    # pro.description="New Description here"
    # pro.save()
    # pro = Promotion(pk=26)
    # pro.delete()
    # pro = Promotion.objects.filter(id__gt=5).delete()
    # cus = Customer.objects.raw('SELECT * FROM store_customer')
    # return render(request,'index.html')
   

# View for Form API
#def home(request):
 #   if request.method == 'POST':
  ##      customer_form = CustomerForm(request.POST)
    #    if customer_form.is_valid():
     #       fname = customer_form.cleaned_data['first_name']
      #      lname = customer_form.cleaned_data['last_name']
       #     email = customer_form.cleaned_data['email']
        #    phoneno = customer_form.cleaned_data['phone_no']
         #   member = customer_form.cleaned_data['membership']
          #  print("Form Validated with POST Data")
           # try:
            #    customer = Customer.objects.create(
             #       first_name=fname,
              #      last_name=lname,
               #     email=email,
                #    phone=phoneno,
                 #   membership=member
               # )
               # customer.save()
               # print(f"Customer {customer} saved successfully.")
           # except IntegrityError:
            #    print(f"Error: Customer with email '{email}' already exists.")
  #  else:
   #     customer_form = CustomerForm()

    #return render(request, 'index.html', {'customer': customer_form})
    
#----- Model FORM VIEW --------------

def home(request):
    if request.method == "POST":
        form = userform(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 "Thank You, your data has been submitted")
    else:
        form = userform()
    return render(request, 'index.html', {'form': form})

