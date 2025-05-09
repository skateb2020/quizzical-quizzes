document.addEventListener('DOMContentLoaded', function(){
    const required = document.querySelectorAll('.input');
    //gets all the quiz_buttons                                                                                                                               
    const quizButton = document.querySelectorAll('.quiz_button');
    for (const i of required){
        i.addEventListener("input", checkSubmit);
    }

    function checkSubmit(){
        for(const i of required){
            str = i.value;
            if (!str.trim().length){
                for (const button of quizButton){
                    button.disabled = true;
                }
                return false
            }
        }
        for (const button of quizButton){
            button.disabled = false;
        }
        return true
    }
    checkSubmit();




    for (const button of quizButton){
        button.disabled = true;
        button.addEventListener('click', (event) =>
            check_quiz(event.target.id));
    }
});

function check_quiz(id){
    console.log("button is clicked");

    //get answers
    let response1 = document.getElementById('id_question1').value.toUpperCase().replace(/\s/g, "");
    let response2 = document.getElementById('id_question2').value.toUpperCase().replace(/\s/g, "");
    let response3 = document.getElementById('id_question3').value.toUpperCase().replace(/\s/g, "");
    let response4 = document.getElementById('id_question4').value.toUpperCase().replace(/\s/g, "");
    let response5 = document.getElementById('id_question5').value.toUpperCase().replace(/\s/g, "");
    let response6 = document.getElementById('id_question6').value.toUpperCase().replace(/\s/g, "");
    let response7 = document.getElementById('id_question7').value.toUpperCase().replace(/\s/g, "");
    let response8 = document.getElementById('id_question8').value.toUpperCase().replace(/\s/g, "");
    let response9 = document.getElementById('id_question9').value.toUpperCase().replace(/\s/g, "");
    let response10 = document.getElementById('id_question10').value.toUpperCase().replace(/\s/g, "");

    //get divs
    let div1 = document.getElementById('div1');
    let div2 = document.getElementById('div2');
    let div3 = document.getElementById('div3');
    let div4 = document.getElementById('div4');
    let div5 = document.getElementById('div5');
    let div6 = document.getElementById('div6');
    let div7 = document.getElementById('div7');
    let div8 = document.getElementById('div8');
    let div9 = document.getElementById('div9');
    let div10 = document.getElementById('div10');

    var correctAnswers = 0;

    //get quiz
    fetch(`/check/${id}`)
    .then(response => response.json())
    .then(quiz => {
        let rightM = "You got this correct. Great job!";
        //checking if the answers are right
        //#1
        let answ1 = quiz.answer1.toUpperCase().replace(/\s/g, "");
        if(answ1 === response1){
            div1.innerHTML = rightM;
            div1.classList.add("correct"); 
            correctAnswers++;
        } else{
            div1.innerHTML = `The correct answer is ${quiz.answer1}. Nice try!`;
            div1.classList.add("incorrect");
        }
        //#2
        let answ2 = quiz.answer2.toUpperCase().replace(/\s/g, "");
        if(answ2 === response2){
            div2.innerHTML = rightM;
            div2.classList.add("correct");
            correctAnswers++;
        } else{
            div2.innerHTML = `The correct answer is ${quiz.answer2}. Nice try!`;
            div2.classList.add("incorrect");
        }
        //#3
        let answ3 = quiz.answer3.toUpperCase().replace(/\s/g, "");
        if(answ3 === response3){
            div3.innerHTML = rightM;
            correctAnswers++;
            div3.classList.add("correct");
        } else{
            div3.innerHTML = `The correct answer is ${quiz.answer3}. Nice try!`;
            div3.classList.add("incorrect");
        }
        //#4
        let answ4 = quiz.answer4.toUpperCase().replace(/\s/g, "");
        if(answ4 === response4){
            div4.innerHTML = rightM;
            correctAnswers++;
            div4.classList.add("correct");
        } else{
            div4.innerHTML = `The correct answer is ${quiz.answer4}. Nice try!`;
            div4.classList.add("incorrect");
        }
        //#5
        let answ5 = quiz.answer5.toUpperCase().replace(/\s/g, "");
        if(answ5 === response5){
            div5.innerHTML = rightM;
            correctAnswers++;
            div5.classList.add("correct");
        } else{
            div5.innerHTML = `The correct answer is ${quiz.answer5}. Nice try!`;
            div5.classList.add("incorrect");
        }
        //#6
        let answ6 = quiz.answer6.toUpperCase().replace(/\s/g, "");
        if(answ6 === response6){
            div6.innerHTML = rightM;
            correctAnswers++;
            div6.classList.add("correct");
        } else{
            div6.innerHTML = `The correct answer is ${quiz.answer6}. Nice try!`;
            div6.classList.add("incorrect");
        }
        //#7
        let answ7 = quiz.answer7.toUpperCase().replace(/\s/g, "");
        if(answ7 === response7){
            div7.innerHTML = rightM;
            correctAnswers++;
            div7.classList.add("correct");
        } else{
            div7.innerHTML = `The correct answer is ${quiz.answer7}. Nice try!`;
            div7.classList.add("incorrect");
        }
        //#8
        let answ8 = quiz.answer8.toUpperCase().replace(/\s/g, "");
        if(answ8 === response8){
            div8.innerHTML = rightM;
            correctAnswers++;
            div8.classList.add("correct");
        } else{
            div8.innerHTML = `The correct answer is ${quiz.answer8}. Nice try!`;
            div8.classList.add("incorrect");
        }
        //#9
        let answ9 = quiz.answer9.toUpperCase().replace(/\s/g, "");
        if(answ9 === response9){
            div9.innerHTML = rightM;
            correctAnswers++;
            div9.classList.add("correct");
        } else{
            div9.innerHTML = `The correct answer is ${quiz.answer9}. Nice try!`;
            div9.classList.add("incorrect");
        }
        //#10
        let answ10 = quiz.answer10.toUpperCase().replace(/\s/g, "");
        if(answ10 === response10){
            div10.innerHTML = rightM;
            correctAnswers++;
            div10.classList.add("correct");
        } else{
            div10.innerHTML = `The correct answer is ${quiz.answer10}. Nice try!`;
            div10.classList.add("incorrect");
        }

        console.log(correctAnswers);
        //display score
        let score = document.getElementById("score");
        score.innerHTML = `Your score is ${correctAnswers}. Great job! :)`;
        score.classList.add("score_style");

         //points
        let newPoints = correctAnswers * 10;
        let currentUser = parseInt(document.getElementById("user_id").value);
        let currentPoints = parseInt(document.getElementById("user_points").value);

        let numOfPoints = currentPoints + newPoints;
        console.log(numOfPoints);

        fetch(`/points/${currentUser}`,{
            method: "PUT", 
            body: JSON.stringify({
                points: numOfPoints
            })
        })
    })
}