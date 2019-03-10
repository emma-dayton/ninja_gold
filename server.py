from flask import Flask, render_template, request, redirect, session
from random import randint
app = Flask(__name__)
app.secret_key = 'a5f29b19f8ca2175b16f5f395ac8955c'
# our index route will handle rendering our form


@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'count' not in session:
        session['count'] = 0
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def process_money():
    print(request.form)
    if request.form['building'] == 'farm':
        session['gold'] += randint(8,13)
    elif request.form['building'] == 'cave':
        session['gold'] += randint(0,30)
        session['count'] += 3
    elif request.form['building'] == 'house':
        session['gold'] += randint(3,15)
    elif request.form['building'] == 'casino':
        session['gold'] += randint(-50, 50)
    session['count'] += 1
    print(session['count'])
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)
