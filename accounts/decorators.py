from django.contrib.auth.decorators import user_passes_test

def admin_required(view_func):
    return user_passes_test(lambda u: u.is_superuser)(view_func)

def salon_required(view_func):
    return user_passes_test(lambda u: getattr(u.profile, 'role', '') == 'salon')(view_func)

def client_required(view_func):
    return user_passes_test(lambda u: getattr(u.profile, 'role', '') == 'client')(view_func)