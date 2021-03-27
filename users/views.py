from django.shortcuts import render,redirect
from django.contrib import  messages
from .forms import UserRegisterForm, UserUpdateForm, pat_ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method=="POST":
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            profile.pat_Profile.firstname = form.cleaned_data.get('firstname')
            profile.pat_Profile.lastname = form.cleaned_data.get('lastname')
            profile.pat_Profile.age = form.cleaned_data.get('age')
            profile.pat_Profile.dob = form.cleaned_data.get('dob')
            profile.pat_Profile.address = form.cleaned_data.get('address')
            profile.pat_Profile.city = form.cleaned_data.get('city')
            profile.pat_Profile.country = form.cleaned_data.get('country')
            profile.pat_Profile.postalcode = form.cleaned_data.get('postalcode')
            profile.pat_Profile.image = request.FILES['image']
            profile.save()
            messages.success(request,f'Your account has been created! Please log in.')
            return redirect('login')
    else: 
        form = UserRegisterForm()
    
    return render(request,'users/register.html',{'form': form})


def pat_register(request):
    if request.method=="POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'Your account has been created! Please log in.')
            return redirect('pat_login')
    else: 
        form = UserRegisterForm()
    
    return render(request,'users/pat_register.html',{'form': form})




@login_required
def pat_profile(request):
    if request.method=="POST":
        u_form = UserUpdateForm(request.POST, instance=request.user.pat_Profile)
        p_form = pat_ProfileUpdateForm(request.POST, request.FILES, instance=request.user.pat_Profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile.html')
    else:
        u_form = UserUpdateForm(instance=request.user.pat_Profile)
        p_form = pat_ProfileUpdateForm(instance=request.user.pat_Profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
     }
    return render(request,'profile.html',context)