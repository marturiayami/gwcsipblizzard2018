/* Buzzfeed Quiz
Create a Buzzfeed Quiz with 5 questions. Create a method for determining what
the results will be. Combine our knowledge of HTML, JS, and CSS to get hired at
Buzzfeed.
1. Finish the function 'creatQuestions'
  a. Make sure you have a list of dictionary of questions
  b. Create the questions and options (aka the radio buttons) DYNAMICALLY
  in JavaScript. In other words, don't hard code the questions; we want to use
  code to access our list of dictionary of questions.
      (HINT 1: HTML is just a bunch of STRINGS. Create HTML code with JS by
      creating strings with tags i.e. ('<input type="radio" name="group" value ="asdf"'))
      (HINT 2: Group the radio button inputs for each question using the SAME name
       or class)
  c. Make sure our changes are reflected in the HTML
      (HINT: getElementById and change its innerHTML)
  d. Call this function WHEN THE PAGE LOADS!!!!
      (HINT: wrap the function in paranthesis like in Overwatch Hero workshop)
2. Define the function 'submitAnswer'
  a. We want to iterate through each group of questions to see what the user
  selected.
  (HINT: a selected answer is "checked"; look up checked radio button)
  b. Determine how your Buzzfeed personality is predicted
      ideas (easy): Assign points to each of your option. If an option makes the
      user a Broccoli, assign a low point (0,1). If an option makes the user a Carrot,
      assign medium high points (4,5). If an option makes the user a Celery,
      assign high points (10). All numbers selected are arbitrary; you decide.
          0-15 points = Broccoli
          16-30 points = Carrot
          30-45 points = Celerey
      ideas (medium):
          Determine which value was selected the MAXIMUM times
          Need to handle TIES.
3. Make more questions, add CSS, add images, use BootStrap
*/
(function creatQuestions(){

  /*: ADD MORE QUESTIONS. Create a field for images*/

  var questions = [
    {
      "question": "What is your favorite book genre?",
      "name": "book genres",
      "answers" : {
        "romance": 8,
        "mystery": 5,
        "realistic fiction": 2
      }
    },
    {
      "question": "What is your favorite listed color?",
      "name": "colors",
      "answers" : {
        "red": 9,
        "blue": 6,
        "green": 3
      }
    },
    {
      "question": "What do you like to do in your free time?",
      "name": "fun",
      "answers" : {
        "read": 8,
        "play video/board games": 4,
        "hangout with friends": 2
      }
    }
  ];

  var html = "";
  for (var i = 0; i < questions.length; i++){
    html += questions[i]["question"] + "<br>" /* TODO: Place your question here*/
    for (var key in questions[i]["answers"]){
      html += '<input type="radio" name="' + questions[i]["name"] + '" value="';
      html += questions[i]["answers"][key] + '">' + key + "<br>";
    }
  }

  /* TODO: set the element "survey" 's innerHTML to html'*/
document.getElementById("quiz").innerHTML= html;

})();

function tacobell(){
  var total = 0;
  var categories = ['book genres', 'colors', 'fun'];

  /*Determine your winning "personality" */

  var score = {
    "math": 0,
    "social studies/istory": 0,
    "language art": 0
  }

  for (var j = 0; j < categories.length; j++){
    var cat = document.getElementsByName(categories[j]);
    for (var i = 0; i < cat.length; i++){
      if (cat[i].checked){
        total += parseInt(cat[i].value);
      }
    }
  }

  var subject;
  if (total < 7){
    subject = "Social Studies/History"
  }
  else if (total < 15){
    subject = "Math"
  }
  else {
    subject = "Language Arts"
  }
  /*Replace the empty quotes with the result of the quiz*/
  document.getElementById("results").innerHTML = "Your best subject is "  + subject;
}
