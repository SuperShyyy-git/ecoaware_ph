from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import User
from .forms import CustomLoginForm, CustomUserCreationForm, CustomUserChangeForm
from django.urls import reverse

# ------------------------
# AUTHENTICATION VIEWS
# ------------------------

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = user.username
            messages.success(request, f'Account created for {username}!')
            return redirect('users:login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})


def user_login(request):
    form = CustomLoginForm()
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {user.username}!')
                return redirect('users:user_dashboard')
        messages.error(request, 'Invalid username or password.')
    return render(request, 'users/login.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('users:login')


# ------------------------
# DASHBOARDS
# ------------------------

@login_required
def user_dashboard(request):
    return render(request, 'users/dashboard.html')


@login_required
def admin_dashboard(request):
    if not request.user.is_staff:
        return redirect('users:access_denied')
    return render(request, 'users/admin_dashboard.html')


# ------------------------
# USER MANAGEMENT (ADMIN)
# ------------------------

@login_required
def user_list(request):
    if not request.user.is_staff:
        return redirect('users:access_denied')
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})


@login_required
def user_edit(request, user_id):
    if not request.user.is_staff:
        return redirect('users:access_denied')
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, f'{user.username} updated successfully.')
            return redirect('users:user_list')
    else:
        form = CustomUserChangeForm(instance=user)
    return render(request, 'users/user_form.html', {'form': form, 'user_obj': user})


@login_required
def toggle_user_status(request, user_id):
    if not request.user.is_staff:
        return redirect('users:access_denied')
    user = get_object_or_404(User, id=user_id)
    user.is_active = not user.is_active
    user.save()
    messages.info(request, f"{user.username}'s status updated.")
    return redirect('users:user_list')


@login_required
def delete_user(request, user_id):
    if not request.user.is_staff:
        return redirect('users:access_denied')
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        messages.success(request, f'{user.username} has been deleted.')
        return redirect('users:user_list')
    return render(request, 'users/user_confirm_delete.html', {'user_obj': user})


# ------------------------
# USER PROFILE
# ------------------------

@login_required
def user_profile(request, username):
    profile_user = get_object_or_404(User, username=username)
    return render(request, 'users/profile.html', {'profile_user': profile_user})


# ------------------------
# ACCESS DENIED PAGE
# ------------------------

def access_denied(request):
    context = {
        'user_list_url': reverse('users:user_list'),
        'admin_dashboard_url': reverse('users:admin_dashboard'),
        'user_dashboard_url': reverse('users:user_dashboard'),
        'login_url': reverse('users:login'),
    }
    return render(request, 'users/access_denied.html', context)