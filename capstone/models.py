from xml.etree.ElementTree import ProcessingInstruction
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class MyProfileManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError("User must have a username.")
        
        user = self.model(
            username=username
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            username=username,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user


class Profile(AbstractBaseUser):
    username                = models.CharField(verbose_name="username", max_length=60, unique=True)
    date_joined             = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login              = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin                = models.BooleanField(default=False)
    is_active               = models.BooleanField(default=True)
    is_staff                = models.BooleanField(default=False)
    is_superuser            = models.BooleanField(default=False)
    points                  = models.IntegerField(blank=True, default=0)

    USERNAME_FIELD = 'username'

    objects = MyProfileManager()

    def _str_(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def serialize(self):
        return{
            "id": self.profile.pk,
            "username": str(self.username),
            "points": int(self.points)
        }

class Quiz(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, default="")
    title = models.TextField(default="")
    description = models.TextField(null=True, blank=True, default="")
    question1 = models.TextField()
    answer1 = models.TextField()
    question2 = models.TextField()
    answer2 = models.TextField(default="")
    question3 = models.TextField()
    answer3 = models.TextField()
    question4 = models.TextField()
    answer4 = models.TextField()
    question5 = models.TextField()
    answer5 = models.TextField()
    question6 = models.TextField()
    answer6 = models.TextField()
    question7 = models.TextField()
    answer7 = models.TextField()
    question8 = models.TextField()
    answer8 = models.TextField()
    question9 = models.TextField()
    answer9 = models.TextField()
    question10 = models.TextField()
    answer10 = models.TextField()
    date_and_time = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField(default=False)

    def serialize(self):
        return{
            "id": self.pk,
            "title": str(self.title),
            "question1": str(self.question1),
            "answer1": str(self.answer1),
            "question2": str(self.question2),
            "answer2": str(self.answer2),
            "question3": str(self.question3),
            "answer3": str(self.answer3),
            "question4": str(self.question4),
            "answer4": str(self.answer4),
            "question5": str(self.question5),
            "answer5": str(self.answer5),
            "question6": str(self.question6),
            "answer6": str(self.answer6),
            "question7": str(self.question7),
            "answer7": str(self.answer7),
            "question8": str(self.answer8),
            "answer8": str(self.answer8),
            "question9": str(self.question9),
            "answer9": str(self.answer9),
            "question10": str(self.question10),
            "answer10": str(self.answer10)
        }


