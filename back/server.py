from flask import Flask, request, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html') #render main html file

@app.route('/login')
def login():
    return render_template('login.html') #render login page

@app.route('/register')
def register():
    return render_template('register.html') #render register page


if __name__== "__main__":
    app.run(debug=True, host='localhost', port=9874)
