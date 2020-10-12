from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Profile
from django.template import loader
from .forms import Registration_Form
from django.contrib.auth.models import User
from AOI.models import Post, AOI
from django.template.defaultfilters import slugify

# Create your views here.


def index(request):
    template = loader.get_template('Profile/index.html')
   # user_pf = Profile.objects.orderby(filter(Profile.user))
    user_pf = Profile.objects.get(name=Profile.name)
    context = {'user_pf':user_pf}


    return HttpResponse(template.render(context, request))

@login_required()
def prof(request):

    user = request.user
    post = Post.objects.all().order_by('-published_date')
    template = loader.get_template('Profile/pf_page.html')
    user_pf = Profile.objects.all()


    reg_form = Registration_Form()
    context = {'reg_form':reg_form,'user_pf':user_pf,'post':post}


    return HttpResponse(template.render(context,request))


@login_required()
def editProf(request):

    template = loader.get_template('Profile/edit_prof.html')
    success_url = loader.get_template('Profile/pf_page.html')

    reg_form = Registration_Form(request.POST, request.FILES, instance=request.user.profile)

    if request.method == 'POST':
        if reg_form.is_valid():

            form = reg_form.save(commit=False)

            form.Profile = form




    else:
        form = Registration_Form(instance=request.user)
        form.save()

        print('')

    context = {'reg_form':reg_form}
    return HttpResponse(template.render(context,request))

