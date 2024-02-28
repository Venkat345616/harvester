from django.shortcuts import render, redirect
from .models import farmers
from django.contrib import messages
from datetime import datetime
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



# Create your views here.


def home(request):
    owners = farmers.objects.values('owner_name').distinct()
    return render(request, "index.html",{'owners': owners})



def farmer(request):
   
    if request.method == 'POST':
        uowner_name = request.POST['owner_name']
        udate = request.POST['date']
        ufarmer_name = request.POST['farmer_name']
        utime = request.POST['time']
        urate = request.POST['rate']
        umobile_number = request.POST['mobile_number']

        if uowner_name == "select":
            messages.info(request, "Please select Owner name")
            return redirect('farmer')
        elif urate == "select":
            messages.info(request, "Please select rate")
            return redirect('farmer')

        try:
            time_worked = datetime.strptime(utime, '%H:%M')
            total = round((time_worked.hour + time_worked.minute / 60) * int(urate))
        except ValueError:
            messages.info(request, "Invalid time format. Please use HH:MM.")
            return redirect('farmer')

      

        user = farmers.objects.create(
            owner_name=uowner_name,
            date=udate,
            farmer_name=ufarmer_name,
            time=utime,
            rate=urate,
            total=total,
            mobile_number=umobile_number
        )
        user.save()
        messages.success(request, "Added successfully")
        return redirect('farmer')
    else:
        return render(request, "farmer.html")

def login(request):
    if request.method == "POST":

        name = request.POST['login_email']
        password = request.POST['loginpswd']


        user = authenticate(request, username = name, password = password)
        if user is not None:
            auth_login(request, user)
            messages.info(request, f"You are logged in as {name}.")
            return redirect("farmer")
        else:
            messages.info(request, "User Not Found")
            
            return redirect('login')
    else:
        return render(request, "login.html")
    
def user_logout(request):
    logout(request)
    return redirect('/')

def owner_details(request, owner_name):
    farmer_objects = farmers.objects.filter(owner_name=owner_name)

    total_time_minutes = sum([(farmer.time.hour * 60) + farmer.time.minute for farmer in farmer_objects])
    total_rate = sum([float(farmer.total) for farmer in farmer_objects])

    total_time_hours, total_time_remainder = divmod(total_time_minutes, 60)
    total_time = f"{total_time_hours} hours {total_time_remainder} minutes"
    return render(request, 'owner_details.html', {'farmer_objects': farmer_objects, 'owner_name': owner_name,
        'total_time': total_time,
        'total_rate': total_rate,})


def search_farmers(request):
    if request.method == 'POST':
        search_query = request.POST.get('search')  

        results = farmers.objects.filter(farmer_name__icontains=search_query)

        return render(request, 'search_farmers.html', {'results': results, 'search_query': search_query})

    return render(request, 'search_farmers.html')

def farmer_details(request, farmer_name):
    farmer_results = farmers.objects.filter(farmer_name=farmer_name)

    total_time_minutes = sum([(farmer.time.hour * 60) + farmer.time.minute for farmer in farmer_results])
    total_rate = sum([float(farmer.total) for farmer in farmer_results])

    total_time_hours, total_time_remainder = divmod(total_time_minutes, 60)
    total_time_formatted = f"{total_time_hours} hours {total_time_remainder} minutes"

    return render(request, 'farmer_details.html', {'farmer_results': farmer_results, 'farmer_name': farmer_name,'total_time': total_time_formatted,
        'total_rate': total_rate,})
       


  

    