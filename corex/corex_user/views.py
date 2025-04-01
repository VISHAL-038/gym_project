from django.shortcuts import render, redirect
from .forms import Step1Form, Step2Form, Step3Form
from .models import CustomUser
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from django.contrib.auth import logout

def register_step1(request):
    if request.method == 'POST':
        form = Step1Form(request.POST)
        if form.is_valid():
            request.session['step1_data'] = form.cleaned_data
            return redirect('register_step2')
    else:
        form = Step1Form()
    return render(request, 'corex_user/register_step1.html', {'form': form})

def register_step2(request):
    if 'step1_data' not in request.session:
        return redirect('register_step1')
    
    if request.method == 'POST':
        form = Step2Form(request.POST)
        if form.is_valid():
            request.session['step2_data'] = form.cleaned_data
            return redirect('register_step3')
    else:
        form = Step2Form()
    return render(request, 'corex_user/register_step2.html', {'form': form})

def register_step3(request):
    if 'step1_data' not in request.session or 'step2_data' not in request.session:
        return redirect('register_step1')
    
    if request.method == 'POST':
        form = Step3Form(request.POST)
        if form.is_valid():
            # Create the user
            user = CustomUser(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                height=form.cleaned_data['height'],
                weight=form.cleaned_data['weight'],
                gender=form.cleaned_data['gender'],
                age=request.session['step2_data']['age'],
                fitness_goals=request.session['step1_data']['fitness_goals'],
            )
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            # Clear session data
            del request.session['step1_data']
            del request.session['step2_data']
            return redirect('profile')
    else:
        form = Step3Form()
    return render(request, 'corex_user/register_step3.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if form.cleaned_data['remember_me']:
                request.session.set_expiry(1209600)  # 2 weeks
            else:
                request.session.set_expiry(0)  # Browser session
            # Check for 'next' parameter, otherwise default to profile
            next_url = request.GET.get('next', 'profile')
            return redirect(next_url)
    else:
        form = LoginForm()
    return render(request, 'corex_user/login.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'corex_user/profile.html', {'user': request.user})


def user_logout(request):
    logout(request)
    return redirect('login')