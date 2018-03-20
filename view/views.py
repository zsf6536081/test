from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponseRedirect,HttpResponse
from view.form import userform
from .models import user

def index(req):
    print(req.path)
    return HttpResponse("haha")

def indexold(req):

    return HttpResponseRedirect('index/a')

def show(req):
    # u=user.objects.filter(username__contains='e')
    k=user.um.showall()
    q=user.fm.get()
    print(q)
    return render(req, 'show.html', {'us': k})


def register(req):
    if req.method == 'POST':
        uf= userform(req.POST)

        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']

            user.objects.create(username=username,password=password)


            # user.save()
            return HttpResponse('reg success')

    else:
        uf = userform()

    return render(req, 'register.html', {'uff': uf})


def login(req):
    if req.method == 'POST':
        uf = userform(req.POST)

        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']

            u=user.objects.filter(username__exact=username, password__exact=password)
            HttpResponse('view success')

            if u:
                return HttpResponse('view success')

            else:
                return HttpResponse("no user")


    else:
        uf = userform()

    return render(req, 'view.html', {'uf': uf})



def main(request):
    user=request.session.get('username',"游客")

    return render(request, 'view/main.html',{'user':user,'k':'1234'})


def logg(request):
    return render(request, 'login.html')


def showmain(request):
    userr=request.POST.get('use')

    request.session['username']=userr
    #request.session.set_expiry(5)
    print(userr)
    return HttpResponseRedirect('main')

from django.contrib.auth import logout

def quit(req):
    #req.session.flush()
    req.session.clear()
    #logout(req)
    return HttpResponseRedirect('main')

def upfile(req):
    return render(req,'upfile.html')


import os
from django.conf import settings
def savefile(req):
    if req.method=="POST":
        f = req.FILES['file']
        fpath= os.path.join(settings.MEDIA_ROOT, f.name)
        with open(fpath, 'wb') as fp:
            for info in f.chunks():
                fp.write(info)


        return HttpResponse("success")
    else:
        return HttpResponse("upload fail")