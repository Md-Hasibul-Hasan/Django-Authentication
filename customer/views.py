from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import logout
from root.decorators import login_and_role_required

# Create your views here.
@login_and_role_required('customer')
def customer_dashboard(request):
    return render(request, 'customer/dashboard.html')

@login_and_role_required('customer')
def password_change_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            logout(request) 
            messages.success(request, 'Your password was successfully updated! Please login again with new password.')
            return redirect('login')
        else:
            for field, errors in form.errors.items():
                print(f"Field: {field}, Errors: {errors}")
                for error in errors:
                    messages.error(request,error)
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'customer/pass_change.html', {'form': form})