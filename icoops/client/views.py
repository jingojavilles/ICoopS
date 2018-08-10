from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpResponse, Http404
from .models import Branch, Client
from .forms import NewTopicForm

def home(request):

   # branches = Branch.objects.all()
    clients = Client.objects.all()
    return render(request, 'home.html', {'clients': clients})


def new_client(request):
    # clien = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            # client = form.save(commit=False)
            # client.save()
            clients = Client.objects.create(
                acctid=form.cleaned_data.get('acctid'),
                fname=form.cleaned_data.get('fname'),
                lname=form.cleaned_data.get('lname'),
                address=form.cleaned_data.get('address'),
                contactnum=form.cleaned_data.get('contactnum'),
                branch=Branch.objects.get(branchcode='01')
            )
            return redirect('view_client', pk=form.cleaned_data.get('acctid'))  # TODO: redirect to the created topic page
    else:
        form = NewTopicForm()
    return render(request, 'new_client.html', {'form': form})

    # client = get_object_or_404(Client, pk=pk)

    # if request.method == 'POST':
    #     acctid = request.POST['acctid']
    #     fname = request.POST['fname']
    #     lname = request.POST['lname']
    #     address = request.POST['address']
    #     contactnum = request.POST['contactnum']
    #     # fname = request.POST['fname']
    #
    #     user = User.objects.first()  # TODO: get the currently logged in user
    #
    #     clients = Client.objects.create(
    #         acctid=acctid,
    #         fname=fname,
    #         lname=lname,
    #         address=address,
    #         contactnum=contactnum,
    #         # fname=fname,
    #     )
    #
    #     # post = Post.objects.create(
    #     #     message=message,
    #     #     topic=topic,
    #     #     created_by=user
    #     # )
    #
    #     return redirect('view_client', pk=client.pk)  # TODO: redirect to the created topic page
    #
    # return render(request, 'new_client.html', {'client': client})


def edit_client(request, pk):
    clien = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = NewTopicForm(request.POST, instance=clien)
        if form.is_valid():
            # client = form.save(commit=False)
            # client.save()
            clients = Client.objects.create(
                acctid=form.cleaned_data.get('acctid'),
                fname=form.cleaned_data.get('fname'),
                lname=form.cleaned_data.get('lname'),
                address=form.cleaned_data.get('address'),
                contactnum=form.cleaned_data.get('contactnum'),
                branch=Branch.objects.get(branchcode='01')
            )
            return redirect('view_client', pk=clien)  # TODO: redirect to the created topic page
    else:
        form = NewTopicForm(instance=clien)
    return render(request, 'new_client.html', {'form': form})


def view_client(request, pk):
    clien = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = NewTopicForm(request.POST, instance=clien)
        if form.is_valid():
            client = form.save(commit=False)
            client.save()
            # clients = Client.objects.create(
            #     acctid=form.cleaned_data.get('acctid'),
            #     fname=form.cleaned_data.get('fname'),
            #     lname=form.cleaned_data.get('lname'),
            #     address=form.cleaned_data.get('address'),
            #     contactnum=form.cleaned_data.get('contactnum'),
            #     branch=Branch.objects.get(branchcode='01')
            # )
            return redirect('view_client', pk=form.cleaned_data.get('acctid'))  # TODO: redirect to the created topic page
    else:
        form = NewTopicForm(instance=clien)
    return render(request, 'viewclient.html', {'form': form, 'client': clien})



    # client = get_object_or_404(Client, pk=pk)
    # return render(request, 'viewclient.html', {'client': client})