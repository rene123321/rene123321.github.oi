from flask import Flask, render_template

app = Flask(name)

# Главная страница
@app.route('/')
def home():
    return '<h1>работает!</h1><p>Мой первый сайт на Python</p>'

@app.route('/about')
def about():
    return '<h1>Обо мне</h1><p>Я научился делать сайты на Python</p>'

if name == 'main':
    app.run(debug=True)
