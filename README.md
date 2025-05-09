<h1>Quizzical Quizzes</h1>
<h2>Description:</h2>

Quizzical Quizzes is an entertaining website where you can take quizzes created by yourself or others. The quizzes can be used for a variety of purposes including studying, trivia, or just for fun. Once you create an account you earn ten points for every question you answer correctly.
<h4>How to Use:</h4>
A user can take quizzes on Quizzical Quizzes without being a member or logged in, but he will not receive points for every question he answers correctly. Once a member, a user can create his own quizzes through the Create Quizzes tab with the option of keeping his quizzes public or private. Private quizzes are only accessible to the user who created them, but public quizzes can be viewed and taken by everyone. When logged in, the user has to press his username to access his account details, including his point count, and all of the quizzes he has created—public and private. The Home tag is the default  page of Quizzical Quizzes, which shows a description of the website along with the ten newest quizzes. On the other hand, the All Quizzes tab shows every public quiz ever created from newest to oldest. Pressing the Random Quiz tab will generate a random public quiz—as mentioned before the quiz creator is the only user who has access to his private quizzes.
<h4>Demo:</h4>
This is a link to my YouTube demo: https://youtu.be/GBorl1yPMUY

<h2>Distinctiveness and Complexity:</h2>

I was inspired to make an entertaining website that could also be used as a tool, depending on the way it is utilized. This project employs Django models to create a custom Profile model to save users and a Quiz model to save quizzes that the users create. My project also uses serialization in Django models to create an API for the quizzes. This API is then used in JavaScript to check a quiz-taker's answers. Depending on whether the answers are correct or incorrect, JavaScript manipulates the DOM to display different messages including the final score. Another API is also used to change the number of points a user has. Along with DOM manipulation and API usage, I also used JavaScript to enable and disable the quiz's submit button. Through JavaScript, the submit button will not enable until all the input fields are filled with anything other than whitespace. In addition to these JavaScript components, my project deploys Django views in unique ways. Every time a quiz page is requested, the order of the questions changes. The user can also request for a random page.

This project is neither a social network nor a e-commerce. Though it allows users to create and save quizzes as in both of those projects, that is the only similarity they share. The main use and majority of the code deals with taking a quiz and checking the answers. It does not include any of the other main elements as the other projects such as comments, bids, following, or likes.

My Capstone project is also mobile responsive. Many checks have especially been put into place so that the Create Quiz page appears beautifully on any mobile device.

<h2>Files:</h2>

This application is in an app called Capstone within a Django project called FinalProject.
<h4>Static Files:</h4>
<ul>
      <li>capstone.js - JavaScript File</li>
    <ul>
      <li>Checks if a quiz can be submitted</li>
      <li>Checks the quiz's inputted answers using a fetch</li>
      <li>Changes the user's points using a fetch</li>
    </ul>
    <br>
  <li>styles.css - entire application's css</li>
    <ul>
      <li>Includes media queries to make the webpage mobile responsive</li>
  </ul>
 </ul>
 
 <h4>Templates:</h4>
 <ul>
      <li>all_quizzes.html - template for the All Quizzes page</li>
      <li>create.html - template for the Create page, where a logged in user can create quizzes</li>
      <li>index.html - template for the default home page, which dispalys a welcome message and the five newest quizzes</li>
      <li>layout.html - contains the JS and CSS files in its head  and displays the webpage header</li>
      <li>login.html - template for the Login page, where registered users can login</li>
      <li>quiz.html -  template for the individually quiz pages, displays all information about the quiz and the questions for the user to answer</li>
      <li>register.html - template for the Register page, where someone can create a new account</li>
      <li>user.html - template that displays all the user's information and all quizzes that he has created</li>
</ul>

<h4>admin.py</h4>
      <ul>
      <li>Registers all the models</li>
      <ul>
      <li>ProfileAdmin</li>
      <li>Profile</li>
      <li>Quiz</li>
      </ul>
     </ul>
     
<h4>forms.py</h4>
      <ul>
      <li>RegistrationForm - form for the user to fill out when making a new account</li>
      <li>ProfileLogin - form for an existing member to fill out when logging in</li>
      <li>QuizForm - form for a logged in member to create a new quiz</li>
      </ul>

<h4>models.py</h4>
<ul>
      <li>MyProfileManager - manager for the Profile Model, creates user profiles and superuser profiles</li>
      <li>Profile - stores users and serializes some of the model fields</li>
      <li>Quiz - stores quizzes that the user creates and serializes all the questions</li>
</ul>

<h4>urls.py</h4>
<ul>
      <li>Includes all of Capstone's paths</li>
      <li>Includes the API routes</li>
 </ul>

<h4>views.py</h4>
<ul>
      <li>index</li>
            <ul>
                  <li>View for default Home page</li>
                  <li>Displays the five newest public quizzes under a welcome message</li>
            </ul>
      <br>
      <li>all_quizzes</li>
            <ul>
                  <li>Displays all the public quizzes from newest to oldest</li>
            </ul>
      <br>
      <li>login_views</li>
            <ul>
                  <li>Displays a login form if the user is not authenticated</li>
                  <li>Redirects an authenticated user</li>
                  <li>Gets the inputs username and password if the form is valid and authenticates the user</li>
            </ul>
            <br>
      <li>register</li>
            <ul>
                  <li>Displays a registration form</li>
                  <li>Saves the form and authenticates the user</li>
            </ul>
            <br>
      <li>logout</li>
            <ul>
                  <li>Logs out a logged in user</li>
            </ul>
      <br>             
      <li>create</li>
      <ul>
            <li>Displays the form for a authenticated user to create a quiz</li>
            <li>Saves a valid form as a Quiz model</li>
      </ul>
      <br>
      <li>quiz</li>
      <ul>
            <li>Displays a specific quiz</li>
            <li>If the quiz is not public, only the user who created the quiz can access this</li>
            <li>Creates a dictionary for the quiz questions and shuffles the order</li>
     </ul>
     <br>
     <li>user</li>
      <ul>
            <li>Only allows the user whose profile it is to access this</li>
            <li>Displays all the quizzes created by the user whose page it is from newest to oldest</li>
      </ul>
      <br>
      <li>check</li>
       <ul>
             <li>Displays a JSONResponse of the serialized quiz information when the method is GET</li>
      </ul>
      <br>
      <li>points</li>
      <ul>
            <li>Displays a serialization of the profile information when the method is GET</li>
            <li>Saves the ppoints when the method is PUT</li>
      </ul>
      <br>
      <li>random_quiz</li>
      <ul>
            <li>Randomly orders all the public quizzes and picks the first one</li>
            <li>Redirects the user to the quiz page of the first quiz</li>
      </ul>
</ul>
      
<h2>How To Run:</h2>
If python is already installed:
<ul>
      <li>python manage.py makemigrations</li>
      <li>python manage.py migrate</li>
      <li>python manage.py runserver</li>
</ul>
If python is not already installed, first download it before following the above steps: <br>
https://www.python.org/downloads/
