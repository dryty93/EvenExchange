# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.template import loader
from Profile.forms import Registration_Form
from django.http import HttpResponse, HttpResponseRedirect


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'Profile/signup.html'


def editProf(request):

    template = loader.get_template('Profile/edit_prof.html')
    success_url = loader.get_template('Profile/pf_page.html')

    reg_form = Registration_Form(request.POST, instance=request.user)

    if request.method == 'POST':

        form = reg_form.save(commit=False)
        form.user = request.user

        form.save()
        form.clear()

        return HttpResponseRedirect("Profile/")


