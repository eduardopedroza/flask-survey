from flask import Flask, render_template, session, redirect, request, flash
# from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey


app = Flask(__name__)
app.secret_key = 'firstapp'
# toolbar = DebugToolbarExtension(app)



responses = []


@app.route('/')
def index():
    """Render the survey introduction page"""
    return render_template('survey_start.html', survey=survey)


@app.route('/start',  methods=["POST"])
def start():
    if not responses:
        session['responses'] = []

    return redirect("/questions/0")


@app.route('/questions/<int:question_id>')
def show_question(question_id):

    if 'responses' not in session:
        return redirect("/start")
    
    if 0 <= question_id < len(survey.questions):
        question = survey.questions[question_id]

        if question_id < len(responses):
            return redirect(f'/questions/{len(responses)}')  
        else:
            return render_template('question.html', question=question)
    else:
        return render_template('question_not_found.html')  



@app.route('/answer', methods=["POST"])
def answer():
    
    choice = request.form.get('answer')
    responses.append(choice)
    index = len(responses)

    if index < len(survey.questions):
        return redirect(f'/questions/{index}')
    else:
        return render_template('complete.html')
    





