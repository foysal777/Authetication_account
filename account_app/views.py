from django.shortcuts import render,redirect
from .forms import registerForm
from django.contrib.auth import authenticate, login , logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import  AuthenticationForm,PasswordChangeForm,SetPasswordForm

# Create your views here.
def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        reg_form = registerForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            user_name = reg_form.cleaned_data.get('username')
            messages.success(request, f' {user_name}  Account Created Successfully Completed ')  
            return redirect('log_in')
        else:
            pass
        
    else:
        reg_form = registerForm()
    return render(request, 'register.html', {'data' : reg_form})   



def log_in(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            log_form = AuthenticationForm(request,request.POST)
           
            if log_form.is_valid():                         
                user_name = log_form.cleaned_data['username']
                pass_word = log_form.cleaned_data['password']
                user = authenticate(username = user_name , password = pass_word )
                if user is not None:
                    login(request, user)              
                    messages.success(request, f' {user_name} logged In successfully Completed')  
                    return redirect('profile')
            else:
                messages.info(request, 'Invalid Username or Password , Try Again...')
            
        else:
            log_form = AuthenticationForm()
       
    else:
        log_form = AuthenticationForm()
    return render(request, 'log_in.html', {'data' : log_form})  



def log_out(request):
    logout(request)
    messages.success(request, 'Logged out Successfully Completed' )
    return redirect('log_in') 




def profile(request):
    if  request.user.is_authenticated:
      return render(request, 'profile.html')




def pass_change(request):
    if  request.user.is_authenticated:
        if request.method == 'POST':
            pass_form = PasswordChangeForm(request.user , data = request.POST )
           
            if pass_form.is_valid():                         
                pass_form.save()
                messages.success(request, 'Your Password is Already Changed Successfully')
                update_session_auth_hash(request, pass_form.user)                         
                return redirect('profile')
            
            
        else:
            pass_form = PasswordChangeForm(request.user)
        return render(request, 'pass_change.html', {'data' : pass_form})  
       
    else:
        return redirect('log_in')



def pass_2(request):
    if  request.user.is_authenticated:
        if request.method == 'POST':
            pass_form = SetPasswordForm(request.user , data = request.POST )
           
            if pass_form.is_valid():                         
                pass_form.save()
                messages.success(request, 'Your Password is Already Changed Successfully')
                update_session_auth_hash(request, pass_form.user)                         
                return redirect('profile')
            
            
        else:
            pass_form = SetPasswordForm(request.user)
        return render(request, 'pass_change.html', {'data' : pass_form})  
       
    else:
        return redirect('log_in')



# https://github.com/phitronio/Conceptual-Sessions-Code/blob/main/Batch-4/Django/Week%204-2/mealProject/accounts/views.py