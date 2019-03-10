from flask import Flask, render_template, request, redirect, session
from random import randint
from datetime import datetime
app = Flask(__name__)
app.secret_key = 'a5f29b19f8ca2175b16f5f395ac8955c'
# our index route will handle rendering our form


@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'count' not in session:
        session['count'] = 15
    if 'log' not in session:
        session['log'] = []
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def process_money():
    print(request.form)
    if session['count'] > 0:
        if request.form['building'] == 'farm':
            gold = randint(10,13)
            session['gold'] += gold
        elif request.form['building'] == 'cave':
            gold = randint(0,40)
            session['gold'] += gold
            session['count'] -= randint(1, 10)
        elif request.form['building'] == 'house':
            gold = randint(3,20)
            session['gold'] += gold
        elif request.form['building'] == 'casino':
            gold = randint(-50, 50)
            session['gold'] += gold
        session['count'] -= 1
        print(session['count'])
        now = datetime.now()
        time = now.strftime("%B %-d, %Y %-I:%M:%S %p")
        if gold >= 0:
            activity = 'Earned ' + str(gold) + " pieces of gold at the " + request.form['building'] + f" ({time})"
        elif gold < 0:
            activity = 'Lost ' + str(gold * -1) + " pieces of gold at the " + request.form['building'] + f" ({time})"
        session['log'].append(activity)
    return redirect('/')

@app.route('/endgame')
def endgame():
    session.pop('gold')
    session.pop('count')
    session.pop('log')
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)
