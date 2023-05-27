from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from.models import*
from django.contrib import messages

def index(request):
    packages = PackageDetails.objects.all()
    return render(request,"index.html",{'packages': packages})
def contact(request):
    return render(request,"contact.html")
def about(request):
    return render(request,'about.html')


    

def signup(request):
    if request.method == 'POST':
        un = request.POST['username']
        fn = request.POST['fname']
        pn = request.POST['pin']
        ag = request.POST['age']
        ad = request.POST['add']
        ln = request.POST['lname']
        en = request.POST['email']
        cn = request.POST['contact_number']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        # Password VAlidation Code here
       
        # Contact No Validation code
        
        # Hover effect on Signup and Signin Button
        if fn.isalpha():
            pass
        else:
            messages.error(request, 'First name field must contain alphabets')
            return redirect('signup')
       
        if pass1 != pass2:
            messages.error(request, 'Passwords does not match')
            return redirect('signup')
        elif Register_table.objects.filter(user__username=un).exists():
            msg='Username already exists'
            return render(request, 'signup.html',{'msg':msg})
        else:
            usr = User.objects.create_user(un, en, pass1)
            usr.first_name = fn
            usr.last_name = ln
            usr.save()
            reg = Register_table(user=usr, contact_number=cn,age=ag,pin=pn,add=ad)
            reg.save()
            return render(request, 'signin.html',
                          {"status": "Dear {} your account created successfully".format(fn)})

    return render(request, 'signup.html')



def signin(request):
    if request.method == 'POST':
        un = request.POST['username']
        pwd = request.POST['pass1']
        user = authenticate(username=un, password=pwd)
        if user:
            login(request, user)
            if user.is_superuser:
                return HttpResponseRedirect("/admin/")
            else:
                return HttpResponseRedirect("/home")
        else:
            messages.error(request, 'Username or password incorrect')
            return render(request, 'signin.html')
    return render(request, 'signin.html')
def logout(request):
    return redirect('travelapp:index')


def feedback(request):
    if request.method == 'POST':
        suggestion = request.POST['suggestion']
        user = request.user.register_table # Assumes the user is authenticated
        
        feedback = Feedback(user=user, suggestion=suggestion)
        feedback.save()
        
        return redirect('travelapp:home')
    else:
       return render(request,'form.html')
    
def blog(request):
     blogs=Blog.objects.all()
     return render(request,'blog.html',{'blogs':blogs})
def home(request):
     packages = PackageDetails.objects.all()
     return render(request,'home.html',{'packages':packages})



def description(request,id):
    description=Blog.objects.filter(id=id)
    return render(request,'description.html',{'description':description})


def book_create(request,pname):
    if request.method == 'POST':
        user = request.user.register_table
        package = request.POST.get('package')
        packages = PackageDetails.objects.get(pname=package)
        

        checkIN= request.POST.get('checkIN')
        checkOut=request.POST.get('checkOut')
        adult=request.POST.get('adult')
        women=request.POST.get('women')
        men=request.POST.get('men')
        kid=request.POST.get('kid')
        if Book.objects.filter(checkIN=checkIN,package=packages):
            msg="THe Package is Already Booked on that Date"
            return render(request,'book.html',{"msg":msg})


        book = Book(user=user, package=packages, checkIN=checkIN,checkOut=checkOut,adult=adult,women=women,men=men,kid=kid,confirm=False)
      
        book.save()
        bookingid=book.id
        book=Book.objects.filter(id=bookingid)
        return render(request,'thankyou.html',{"book":book})
    packageid=PackageDetails.objects.filter(pname=pname)
    pacakagenames=PackageDetails.objects.filter(pname=pname)
    all={
        'a':pacakagenames,
        'packageid':packageid
}
  
    return render(request, 'book.html',all)

def place(request):
     places=Places.objects.all()
     return render(request,'places.html',{'places':places})

def payment(request):
     return render(request,'payment.html')


def search(request):
    if request.method=='GET':
        query=request.GET.get('query')
        if query:
            packages=PackageDetails.objects.filter(amount=query)
            return render(request,'search.html',{'packages':packages})
        else:
            print("no information to show ")
            return request(request,'search.html',{})
def thankyou(request):
    return render(request,'thankyou.html')
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

@login_required
def update_profile(request):
    user = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        user.username = username
        user.email = email
        user.first_name = first_name
        user.last_name=last_name
        user.save()
        return redirect('travelapp:profile')
    return render(request, 'update_profile.html', {'user': user})

def profile(request):
    return render(request,'profile.html')

from django.shortcuts import render, redirect
from .models import PackageDetails, Rating

def rating(request, pname):
    if request.method == 'POST':
        user = request.user.register_table
        package_name = request.POST['package']
        package = PackageDetails.objects.get(pname=package_name)
        review = request.POST['review']
        rate = Rating(user=user, package=package,  review=review)
        rate.save()
        return redirect('travelapp:home')  # Redirect to the thankyou page
    package_names = PackageDetails.objects.filter(pname=pname)
    context = {
        'user': request.user.username,  # Pass the username to the template
        'packages': package_names,
    }
    return render(request, 'rating.html', context)
def bookview(request):
   user=request.user.register_table
   books=Book.objects.filter(user=user)
   return render(request,'booklist.html',{'books':books})
    
def delete(request,id):
    
    package=Book.objects.get(id=id)
    package.delete()
    return redirect('/list/')

from django.shortcuts import render, redirect
from .models import Book

def confirm_order(request, id):
    book=Book.objects.filter(id=id)
    booking = Book.objects.get(id=id)
    booking.confirm = True
    booking.save()
    return render(request,'thankyou.html',{"book":book})

