from django.urls import path
from . import views

urlpatterns=[
    path("", views.index, name="index"),
    path("login", views.login_views, name="login"),
    path("register", views.register, name="register"),
    path("logout", views.logout_view, name="logout"), 
    path("create", views.create, name="create"),
    path("all_quizzes", views.all_quizzes, name="all_quizzes"),
    path("quiz/<int:quiz_id>", views.quiz, name="quiz"),
    path("user/<int:user_id>", views.user, name="user"),
    path("random_quiz", views.random_quiz, name="random_quiz"),

    #API routes
    path("check/<int:quiz_id>", views.check, name="check"),
    path("points/<int:user_id>", views.points, name="points")
]