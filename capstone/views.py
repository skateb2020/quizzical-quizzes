from msilib.schema import PublishComponent
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .models import Profile, Quiz
from .forms import RegistrationForm, ProfileLogin, QuizForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import random
from django.forms.models import model_to_dict
import json
from django.views.decorators.csrf import csrf_exempt
from random import shuffle, choice

# Create your views here.
def index(request):
    public_quizzes = Quiz.objects.filter(public=True)
    quizzes = public_quizzes.all().order_by('-date_and_time')[:5]
    return render(request, "capstone/index.html",{
        "quizzes": quizzes
    })

def all_quizzes(request):
    public_quizzes = Quiz.objects.filter(public=True)
    quizzes = public_quizzes.all().order_by('-date_and_time')
    return render(request, "capstone/all_quizzes.html",{
        "quizzes": quizzes
    })


def login_views(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('index')

    if request.POST:
        login_form = ProfileLogin(request.POST)
        if login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect('index')

    else:
        login_form = ProfileLogin()

    context['login_form'] = login_form
    return render(request, "capstone/login.html", context)

def register(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            profile = authenticate(username=username, password=password)
            login(request, profile)
            return redirect("index")
        else:
            context['registraion_form'] = form
    else:
        form = RegistrationForm()
    return render(request, 'capstone/register.html',{
        "registration_form": form
    })

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('index')

@login_required(login_url='login')
def create(request):
    if request.method == "POST":
        quiz_form = QuizForm(request.POST)
        if quiz_form.is_valid():
            quiz = quiz_form.save(commit=False)
            quiz.user = request.user
            quiz.date_and_time = timezone.now()
            quiz.save()
            return redirect("index")
        else:
            return render(request, "capstone/create.html",{
                "quiz_form": quiz
            })
    quiz_form = QuizForm
    return render(request, "capstone/create.html",{
        "quiz_form": quiz_form
    })

def quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz.objects, pk=quiz_id)
    
    if quiz.public == False:
        author = quiz.user
        if request.user != author:
             return HttpResponse("Access denied.")

    quiz_values = model_to_dict(quiz)
    quiz_questions = []
    for i in range(1, 11):
        quiz_questions.append((i, quiz_values['question' + str(i)]))
    shuffle(quiz_questions)
    print(quiz_questions)
    return render(request, "capstone/quiz.html", {
        "quiz": quiz,
        "quiz_questions": quiz_questions
        })

@login_required(login_url='login')
def user(request, user_id):
    user = get_object_or_404(Profile.objects, pk=user_id)
    if request.user != user:
        return HttpResponse("Access denied.")   
    quizzes = Quiz.objects.filter(user=user).order_by('-date_and_time')   
    return render(request, "capstone/user.html",{
            "user": user,
            "quizzes": quizzes
        })

def check(request, quiz_id):
    try:
        quiz = Quiz.objects.get(pk=quiz_id)
    except Quiz.DoesNotExist:
        return JsonResponse({"error": "Quiz not found."})

    if request.method == "GET":
        return JsonResponse(quiz.serialize())

    else:
        return JsonResponse({"error": "Need a GET request."})

@csrf_exempt
def points(request, user_id):
    try: 
        user = Profile.objects.get(pk=user_id)
    except Profile.DoesNotExist: 
        return JsonResponse({"error": "Profile not found."})

    
    if request.method == "GET":
        return JsonResponse(user.serialize())

    elif request.method == "PUT":
        data = json.loads(request.body)
        user.points = data["points"]
        user.save()

    else:
        return JsonResponse({"error": "Need a GET request."})

def random_quiz(request):
    public_quizzes = Quiz.objects.filter(public=True).order_by("?").first()
    pk = public_quizzes.pk
    return redirect("quiz", quiz_id=pk)
    