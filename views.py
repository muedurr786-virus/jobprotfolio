 from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Sum


def registerpage(req):
    if req.method == 'POST':
        form = UserModelForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserModelForm()
    con = {
        'form': form,
        'Form_titel': 'Register Page',
        'btn': 'Register'
    }

    return render(req, 'auth/baseForm.html',con)



def loginpage(req):
    if req.method == 'POST':
        form = Authform(req, data=req.POST) 
        if form.is_valid():
            user = form.get_user()
            login(req, user)  
            return redirect('dashboard')  
    else:
        form = Authform()
        
    con = {
        'form': form,
        'Form_titel': 'Login Page',  
        'btn': 'Login'              
    }
    return render(req, 'auth/baseForm.html', con)

def logoutpage(req):
    logout(req)
    return redirect('login')

@login_required  
def dashboard(req):
    try:
        profile_obj = UpdateProfiel.objects.get(user=req.user)
        take_bmr = profile_obj.bmr if profile_obj.bmr is not None else 0
    except UpdateProfiel.DoesNotExist:
        take_bmr = 0 


    consume_calory = FoodItemModel.objects.filter(user=req.user).aggregate(total_calori=Sum('calory'))['total_calori'] or 0
    
    need_calory = take_bmr - consume_calory
    data = UpdateProfiel.objects.filter(user=req.user) 
    
    con = {
        'data': data,
        'take_bmr': round(take_bmr, 2),
        'consume_calory': round(consume_calory, 2),
        'need_calory': round(need_calory, 2)
    }
    return render(req, 'dashboard.html', con)

@login_required
def updateprofilepage(req):
    user_profile, created = UpdateProfiel.objects.get_or_create(user=req.user)
    
    if req.method == 'POST':
        form = UpdatedProfileForm(req.POST, req.FILES, instance=user_profile)
        if form.is_valid():
            data = form.save(commit=False)
            weight = data.weight if data.weight is not None else 0
            height = data.height if data.height is not None else 0
            age = data.age if data.age is not None else 0
            
            if data.gender == 'M':
                data.bmr = 66.47 + (13.75 * weight) + (5.003 * height) - (6.755 * age)
            else:
                data.bmr = 655.1 + (9.563 * weight) + (1.850 * height) - (4.676 * age)
            
            data.save()
            return redirect('dashboard')
    else:
        form = UpdatedProfileForm(instance=user_profile)
        
    con = {
        'form': form,
        'title': 'Update Profile',
        'btn_title': 'Update'
    }

    return render(req, 'baseform.html', con)

@login_required
def consumeCaloryPage(req):
    if req.method == 'POST':
        form = FoodItemForm(req.POST)
        if form.is_valid():
            data =form.save(commit=False)
            data.user = req.user
            data.save()
            return redirect('dashboard')
    else:
        form = FoodItemForm()
    con = {
        'form': form,
        'title': 'Consume Calory',
        'btn_title': 'Consume'
    }
        
    return render(req, 'baseform.html', con)





