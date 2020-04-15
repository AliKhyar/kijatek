from django.shortcuts import render, redirect
from .forms import LogInForm, CommentForm
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import *
from django.http import HttpResponse, HttpResponseRedirect, request
from django.urls import reverse


# Create your views here.

def home_page(request):
    disciplines = Discipline.objects.all()
    cities = City.objects.all()
    context = {
        "disciplines": disciplines,
        "cities": cities
    }

    if request.method == 'POST':
        bac_plus = request.POST['bac_plus']
        discipline = request.POST['discipline']
        city = request.POST['city']
        return redirect(f'search_info/data={bac_plus}+{discipline}+{city}') #redirect(search_info(request,bac_plus, department, city))  #, kwargs={'request':request,'bac_plus':bac_plus, 'department':department, 'city':city})

    return render(request,
                    template_name = "core/index.html",
                    context=context)


def search():
    pass

@csrf_exempt
def search_info(request, bac_plus, discipline, city):
    departments = Department.objects.filter(establishment__city=city, bac_plus=bac_plus )#, discipline__name=discipline)   #(discipline=discipline, bac_plus=bac_plus, )
    info = {
        'bac_plus':bac_plus, 
        'discipline':Discipline.objects.filter(id=discipline)[0], 
        'city':City.objects.filter(id=city)[0]
        }
    context = {
        'departments': departments,
        'info':info
    }

    return render(request,
                    template_name = "core/search_info.html",
                    context=context)

"""
def search_info(request, bac_plus, department, city):
    departments = Department.objects.filter(bac_plus=bac_plus, department=department, \
        establishment_id__city_id=city)  #establishment_id__establishment_type__in=establishment_type
    print(bac_plus, department, city)
    return render(request,
                    template_name = "core/khliha.html",
                    context={})

"""






"""
def forum(request):
    questions_replies = dict()
    for q in Question.objects.all():
        replies = Reply.filter(question=q.id)
        questions_replies[q] = replies
    context = {
        'questions_replies':questions_replies
        }
    return render(request = request,
                  template_name='core/forum.html',
                  context = context)

def add_question(request, forum_id,exo):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment=form.data['comment']
        new_comment = Comment(forum=forum_id, user=request.user, body=comment, created=datetime.datetime.now() )
        new_comment.save()

        print('add comment redirection')
        return redirect(f'{exo.type_exo}/{exo.slug}')

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
                    context={"form":form})"""