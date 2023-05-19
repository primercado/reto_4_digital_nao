from flask import render_template, request
from modelos import OpenAIModel

openai_model = OpenAIModel()

def home():
    if request.method == 'GET':
        return render_template('index.html')
    if request.form['question']:
        question = request.form['question']
        answer = openai_model.generate_response(question)
        return render_template('index.html', chat=openai_model.conversations)
    else:
        return render_template('index.html')
