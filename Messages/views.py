from django.shortcuts import render,HttpResponse
from .forms import Message_Form
from .models import User,Profile, Message
from django.template import loader
# Create your views here.

def view_inbox(request):

    inbox = Message.objects.all()
    user = request.user

    profile = user.profile

    template = loader.get_template("Messages/inbox.html")
    inb = Message.objects.filter(receiver_id=user.profile.pk)
    one_message = Message.objects.values('id')

    rec = Message.objects.values('receiver')

    print(one_message)
    context = {'inb': inb}

    return HttpResponse(template.render(context, request))


def sendMessage(request):

    template = loader.get_template('Messages/outbox.html')
    user = request.user
    receiver = request.POST.get('receiver_id')
    message_form = Message_Form(request.POST)
    context = {'messages':message_form}
    if request.method == "POST":
        if message_form.is_valid():
            print('valid')
            form = message_form.save(commit=False)
            template = loader.get_template("Messages/inbox.html")

            form.sender = user
            form.save()

            return HttpResponse(template.render(context, request))

    else:
        return HttpResponse(template.render(context, request))
