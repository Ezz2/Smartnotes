from datetime import datetime
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect

# class SignupView(CreateView):
    # form_class = UserCreationForm
    # template_name = 'home/register.html'
    # success_url = '/smart/notes'

    # def get(self, request, *args, **kwargs):
    #     if self.request.user.is_authenticated:
    #         return redirect('home')
    #     return super().get(request, *args, **kwargs)

    # def form_valid(self, form):
    #     # commit=False: create an object but doesn't save it in database
    #     self.object = form.save(commit=False) 
    #     self.object.user = self.request.user
    #     self.object.save()
    #     return HttpResponseRedirect('/smart/notes')


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, "home/register.html", {"form": form})

class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'

class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'
    success_url = "/"

class HomeView(TemplateView):
    template_name = 'home/welcome.html' 
    extra_context = {'today': datetime.today()}
