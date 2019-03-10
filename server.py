from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'a5f29b19f8ca2175b16f5f395ac8955c'
# our index route will handle rendering our form


@app.route('/')
def index():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)
