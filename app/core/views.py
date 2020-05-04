from django.shortcuts import render, redirect
from .forms import LogInForm, CommentForm
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import *
from django.http import HttpResponse, HttpResponseRedirect, request
from django.urls import reverse
import datetime
from . import bokeh_graph


# Create your views here.

# in context: disciplines and cities => for home.html
#  redirect to search info with bac_plus discipline city
def home_page(request):
    disciplines = Discipline.objects.all()
    cities = City.objects.all()
    context = {
        "disciplines": disciplines,
        "cities": cities
    }

    if request.method == 'POST':
        # extract data to pass it to url
        bac_plus = request.POST['bac_plus']
        discipline = request.POST['discipline']
        city = request.POST['city']
        # redirect(search_info(request,bac_plus, department, city))  #, kwargs={'request':request,'bac_plus':bac_plus, 'department':department, 'city':city})
        return redirect(f'search/data={bac_plus}+{discipline}+{city}')

    return render(request,
                  template_name="core/home.html",
                  context=context)


@csrf_exempt
# called by home_page view
def search_info(request, bac_plus, discipline, city):
    # get all departments where conditions are satisfied
    departments = Department.objects.filter(
        establishment__city=city, bac_plus=bac_plus)
    # info to display in top of search_info.html
    info = {
        'bac_plus': bac_plus,
        'discipline': Discipline.objects.filter(id=discipline)[0],
        'city': City.objects.filter(id=city)[0]
    }
    context = {

        'departments': departments,
        'info': info
    }
    return render(request,
                  template_name="core/search_info.html",
                  context=context)


# return desired establishment info with departments
def search_establishment(request, establishment_id):
    establishment = Establishment.objects.filter(id=establishment_id)[0]
    departments = Department.objects.filter(establishment=establishment)
    context = {
        'establishment': establishment,
        'departments': departments,
        'script': bokeh_graph.script,
        'div': bokeh_graph.div
    }
    return render(request,
                  template_name="core/establishment.html",
                  context=context)

# return desired department info with comments


def search_department(request, establishment_id, department_id):
    department = Department.objects.filter(
        id=department_id, establishment=establishment_id)[0]
    comments_replies = dict()
    comments = Comment.objects.filter(department=department.id)
    for c in comments:
        comments_replies[c] = Reply.objects.filter(comment=c.id)
    context = {
        'department': department,
        'comments_replies': comments_replies
    }
    if request.method == 'POST':
        add_comment(request, department)

    context['comment_form'] = CommentForm()
    return render(request,
                  template_name="core/department.html",
                  context=context)


def all_establishments(request):
    establishments = Establishment.objects.all()
    context = {
        "establishments": establishments,
    }
    
    return render(request, 
    "core/establishments.html", 
    context=context,)

def all_departments(request):
    departments = Department.objects.all()
    context = {
        "departments": departments,
        "for_all":True,
    }
    return render(request, 
    "core/departments.html", 
    context=context,)

def add_comment(request, department):
    form = CommentForm(request.POST)
    # test always passed
    # not true though!
    if True:
        comment = form.data['comment']
        new_comment = Comment(department=department, user=request.user,
                              body=comment, created=datetime.datetime.now())
        new_comment.save()
        return redirect(f"establishments/departments/data={department.establishment.id}+{department.id}")

# view for testing code in test.html and test/ url


def test(request):

    context = {
        'script': bokeh_graph.script,
        'div': bokeh_graph.div
    }
    return render(request,
                  template_name="core/test.html",
                  context=context)


"""
def forum(request)                                                : 
    questions_replies                                             = dict()
    for q in Question.objects.all()                               : 
        replies                                                   = Reply.filter(question=q.id)
        questions_replies[q]                                      = replies
    context = {
        'questions_replies'                                       : questions_replies
        }
    return render(request                                         = request,
                  template_name                                   = 'core/forum.html',
                  context                                         = context)

def add_question(request, forum_id,exo)                           : 
    form                                                          = CommentForm(request.POST)
    if form.is_valid()                                            : 
        comment                                                   = form.data['comment']
        new_comment                                               = Comment(forum=forum_id, user=request.user, body=comment, created=datetime.datetime.now() )
        new_comment.save()

        print('add comment redirection')
        return redirect(f'{exo.type_exo}/{exo.slug}')

@csrf_exempt
def login_page(request)                                           : 
    if request.method == 'POST':
        form                                                      = LogInForm(data=request.POST)
        if form.is_valid()                                        : 
            username                                              = form.cleaned_data.get('username')
            password                                              = form.cleaned_data.get('password')
            user                                                  = authenticate(username=username, password=password)
            if user is not None                                   : 
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect(to                                = "")
            else                                                  : 
                messages.error(request, "Invalid username or password.")
        else                                                      : 
            messages.error(request, "Invalid username or password.")
    form                                                          = LogInForm()
    return render(request                                         = request,
                    template_name                                 = "core/login.html",
                    context                                       = {"form":form})"""
