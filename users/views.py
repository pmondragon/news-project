from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm
# Create your views here.

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('/users/login')
    template_name = 'signup.html'
