from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import Profile, Quiz

class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=60)

    class Meta:
        model = Profile
        fields = ("username", "password1", "password2")

class ProfileLogin(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    class Meta:
        model = Profile
        fields = ("username", "password")

    def clean(self):
        username = self.cleaned_data.get('username', None)
        password = self.cleaned_data.get('password', None)
        if not authenticate(username=username, password=password):
            raise forms.ValidationError("Invalid username and/or password.")
        return None

class QuizForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(QuizForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = 'Title'
        self.fields['description'].label = 'Description'
        self.fields['question1'].label = 'Question 1'
        self.fields['answer1'].label = 'Answer 1'
        self.fields['question2'].label = 'Question 2'
        self.fields['answer2'].label = 'Answer 2'
        self.fields['question3'].label = 'Question 3'
        self.fields['answer3'].label = 'Answer 3'
        self.fields['question4'].label = 'Question 4'
        self.fields['answer4'].label = 'Answer 4'
        self.fields['question5'].label = 'Question 5'
        self.fields['answer5'].label = 'Answer 5'
        self.fields['question6'].label = 'Question 6'
        self.fields['answer6'].label = 'Answer 6'
        self.fields['question7'].label = 'Question 7'
        self.fields['answer7'].label = 'Answer 7'
        self.fields['question8'].label = 'Question 8'
        self.fields['answer8'].label = 'Answer 8'
        self.fields['question9'].label = 'Question 9'
        self.fields['answer9'].label = 'Answer 9'
        self.fields['question10'].label = 'Question 10'
        self.fields['answer10'].label = 'Answer 10'
      

    class Meta:
        model = Quiz
        fields = ['title', 'description', 'question1', 'answer1', 'question2', 'answer2', 'question3', 'answer3', 'question4', 'answer4', 'question5', 'answer5', 'question6', 'answer6', 'question7', 'answer7', 'question8', 'answer8', 'question9', 'answer9', 'question10', 'answer10', 'public']
        help_texts = {"public": "Check to make your quiz visible to everyone."}
        widgets = {"title": forms.Textarea(attrs={"placeholder": "Add your quiz's title here.", "rows":3, "class": "title-field"}),
                    "description": forms.Textarea(attrs={"placeholder": "Add an optional description of your quiz here.", "rows":3, "cols":150, "class": "quiz_field"}),
                    "question1": forms.Textarea(attrs={"placeholder": "Add your first question here.", "rows":3, "cols":150, "class": "quiz_field"}),
                    "answer1": forms.Textarea(attrs={"placeholder": "Add the answer to your first question here.", "rows":3, "cols":150, "class": "quiz_field"}),
                    "question2": forms.Textarea(attrs={"placeholder": "Add your second question here.", "rows":3, "cols":150, "class": "quiz_field"}),
                    "answer2": forms.Textarea(attrs={"placeholder": "Add the answer to your second question here.", "rows":3, "cols":150, "class": "quiz_field"}),
                    "question3": forms.Textarea(attrs={"placeholder": "Add your third question here.", "rows":3, "cols":150, "class": "quiz_field"}),
                    "answer3": forms.Textarea(attrs={"placeholder": "Add the answer to your third question here.", "rows":3, "cols":150, "class": "quiz_field"}),
                    "question4": forms.Textarea(attrs={"placeholder": "Add your fourth question here.", "rows":3, "cols":150, "class": "quiz_field"}),
                    "answer4": forms.Textarea(attrs={"placeholder": "Add the answer to your fourth question here.", "rows":3, "cols":150, "class": "quiz_field"}),
                    "question5": forms.Textarea(attrs={"placeholder": "Add your fifth question here.", "rows":3, "cols":150, "class": "quiz_field"}),
                    "answer5": forms.Textarea(attrs={"placeholder": "Add the answer to your fifth question here.", "rows":3, "cols":150, "class": "quiz_field"}),
                    "question6": forms.Textarea(attrs={"placeholder": "Add your sixth question here.", "rows":3, "cols":150, "class": "quiz_field"}),
                    "answer6": forms.Textarea(attrs={"placeholder": "Add the answer to your sixth question here.", "rows":3, "cols":150, "class": "quiz_field"}),
                    "question7": forms.Textarea(attrs={"placeholder": "Add your seventh question here.", "rows":3, "cols":150, "class": "quiz_field"}),
                    "answer7": forms.Textarea(attrs={"placeholder": "Add the answer to your seventh question here.", "rows":3, "cols":150, "class": "quiz_field"}),
                    "question8": forms.Textarea(attrs={"placeholder": "Add your eighth question here.", "rows":3, "cols":150, "class": "quiz_field"}),
                    "answer8": forms.Textarea(attrs={"placeholder": "Add the answer to your eighth question here.", "rows":3, "cols":150, "class": "quiz_field"}),
                    "question9": forms.Textarea(attrs={"placeholder": "Add your ninth question here.", "rows":3, "cols":150, "class": "quiz_field"}),
                    "answer9": forms.Textarea(attrs={"placeholder": "Add the answer to your ninth question here.", "rows":3, "cols":150, "class": "quiz_field"}),
                    "question10": forms.Textarea(attrs={"placeholder": "Add your tenth question here.", "rows":3, "cols":150, "class": "quiz_field"}),
                    "answer10": forms.Textarea(attrs={"placeholder": "Add the answer to your tenth question here.", "rows":3, "cols":150, "class": "quiz_field"}),
                    "public": forms.CheckboxInput(attrs={"id": "checkbox"})
                    }
                
    

