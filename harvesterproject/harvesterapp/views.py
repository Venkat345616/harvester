from django.shortcuts import render, redirect
from .models import farmers
from django.contrib import messages
from datetime import datetime
# Create your views here.


def home(request):
    if request.method == 'POST':
        uowner_name = request.POST['owner_name']
        udate = request.POST['date']
        ufarmer_name = request.POST['farmer_name']
        utime = request.POST['time']
        urate = request.POST['rate']
        umobile_number = request.POST['mobile_number']

        if uowner_name == "select":
            messages.info(request, "Please select Owner name")
            return redirect('home')
        elif urate == "select":
            messages.info(request, "Please select rate")
            return redirect('home')

        try:
            
            time_worked = datetime.strptime(utime, '%H:%M')
            total = (time_worked.hour + time_worked.minute / 60) * int(urate)
        except ValueError:
            messages.info(request, "Invalid time format. Please use HH:MM.")
            return redirect('home')

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
        return redirect('home')

    return render(request, 'index.html')