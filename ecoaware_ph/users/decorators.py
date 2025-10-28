from django.shortcuts import redirect
from django.contrib import messages
from functools import wraps

def admin_required(view_func):
    """
    Decorator to restrict access to admin users only.
    Redirects to access denied page if user is not admin.
    """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and getattr(request.user, "role", None) == "admin":
            return view_func(request, *args, **kwargs)
        messages.error(request, "Access denied: Admins only.")
        return redirect('users:access_denied')
    return _wrapped_view
