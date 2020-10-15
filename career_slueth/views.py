#from django.views import generic
from django.views.generic import *


class Index(TemplateView):
    template_name= "index.html"

class Dashboard(TemplateView):
    template_name= "dashboard.html"

#class SignUpView(generic.CreateView):
#    form_class = UserCreationForm
#    success_url = reverse_lazy('login')
#    template_name = 'signup.html'
def signup(response):
    return render

class LoginView(TemplateView):
    template_name= 'login.html'
