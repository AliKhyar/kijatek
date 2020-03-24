from django.shortcuts import render, redirect
from .forms import LogInForm
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

# Create your views here.

@csrf_exempt
def login_page(request):
    if request.method == 'POST':
        form = LogInForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect(to="")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = LogInForm()
    return render(request = request,
                    template_name = "core/login.html",
                    context={"form":form})