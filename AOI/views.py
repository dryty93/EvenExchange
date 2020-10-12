from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponse
from .forms import POST_FORM,AOI_FORM,Comment_Form
from django.template import loader
from .models import AOI,Post,Comment
from django.contrib.auth.models import User
from Profile.models import Profile
from django.forms.models import model_to_dict
from django.views.generic import ListView
from django.http import HttpResponseRedirect,JsonResponse

def search_res(request):
    template = loader.get_template("AOI/srch_res.html")



    aois = AOI.objects.values('name')
    aoisss = AOI.objects.values('id')
    all_aois =  AOI.objects.values('summary')
    aoi_img = AOI.objects.values('thumbnail')
    aoi_list= []
    for items in aois:
    # add names of individual aois to list

        aoi_list.append(str(items).split(":")[-1].split("}")[0].split("'")[1])

    #print(aoi_list,aoisss)


    context = { 'aois':aoi_list, 'aoisss': aoisss, 'aoi_all': all_aois, 'n':'n'}

    if request.method == 'POST':

       search = request.POST['search_bar']
       search = str(search)[0].upper() + search[:]

       search = search[0]+search[2:]

       try:
           find = AOI.objects.get(name=search)

       except:
           for things in aoi_list:
               if search in things:
                  search=things
                  find = AOI.objects.get(name=search)





       aoi_len =  len(aoi_list)
       found = True



       context = { 'found': found,'aois': aoi_list, 'search':search, 'aoisss': aoisss, 'aoi_all': all_aois, 'len' : aoi_len, 'find': find}

    return HttpResponse(template.render(context,request))




def one_aoi(request, aoi_id):

    template = loader.get_template("AOI/one_aoi.html")

    id = aoi_id
    posts =Post.objects.filter(aoi_id=id)
    aoi = AOI.objects.get(id=id)
    comment = Comment.objects.all()
    comment_form = Comment_Form(request.POST)
    user = request.user

    if request.method == 'POST':

        if comment_form.is_valid():
            newComment = comment_form.save(commit=False)
            newComment.author = user
            profile = user.profile
            profile.chi += 2
            profile.save()
            newComment.save()

    context = {'aoi': aoi, 'posts': posts, 'comment': comment, 'comment_form': comment_form}


    return HttpResponse(template.render(context, request))


def index(request):

    success = loader.get_template("AOI/query.html")

    if request.method == 'POST':
        query = request.POST['search_bar']
        aoi_items = AOI.objects.get(name=query)
        print(Post.get(pk=Post.aoi), 'h')
        queried_content = Post.objects.get(aoi=aoi_items.name)
        print(aoi_items)
        context = {'items':aoi_items, }
        return HttpResponse(success.render(context,request))


    else:

        comment_form = Comment_Form(request.POST)
        template = loader.get_template("AOI/aoi.html")
        all_content = Post.objects.all()
        all = AOI.objects.all()


        queries = Post.objects.filter()
        data = Post.objects.values('text')
        comment = Comment.objects.all()

        context = {'data':data,'queries':queries,
                   'all_content':all_content,'comment':comment,
                   'all':all,"comment_form":comment_form}


        return HttpResponse(template.render(context,request))

@login_required()
def addAOI(request):

    template = loader.get_template("AOI/addAOI.html")
    aoi_page = loader.get_template("AOI/aoi.html")
    aoi = AOI_FORM()
    aoi_form = AOI_FORM(request.POST, request.FILES)
    user = request.user
    all_aois = list(AOI.objects.all().values())

   # diction = dict()
    context = {'reg_form': aoi_form,'aoi':aoi,'aoi_form':aoi_form}

    if request.method == 'POST':
        if aoi_form.is_valid():
            profile = user.profile

            new_aoi = aoi_form.save(commit=False)
            new_aoi.author = user

            profile.chi += 2
            new_aoi.save()

            context = {'reg_form': aoi_form, 'aoi': aoi, 'aoi_form': aoi_form}

            return HttpResponse(aoi_page.render(context, request))

    else:
        form = aoi_form
        form.save()
        print('')
        context = {'aoi_form': form,'aoi':aoi}
        return HttpResponse(template.render(context, request))

@login_required
def del_post(request):
    user = request.user
    template = loader.get_template("AOI/del_post.html")
    profile = user.profile
    posts =Post.objects.filter(aoi_id=user.profile.pk)
    print(posts)
    context = {'posts': posts, 'pf': profile}



    print(posts)

    return HttpResponseRedirect("/Profile")


@login_required
def addPost(request):
    form = POST_FORM(request.POST)
    user = request.user
    template = loader.get_template("AOI/addPost.html")

    if request.method =='POST':
        if form.is_valid():
            print('val')
            newPost = form.save(commit=False)
            newPost.author = user
            profile = user.profile
            profile.chi += 2
            profile.save()
            #request.user.Profile.chi.save(commit=False)
            #request.user.Profile.chi.save()


            newPost.save()
            context = {'form' : form}

            return HttpResponseRedirect('/AOI')

        else:
            context = {'form':form}
            return HttpResponse(template.render(context,request))

    else:
        context = {'form':form}
        return HttpResponse(template.render(context, request))


