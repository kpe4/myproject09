from flask import Flask
from flask import request
from markupsafe import escape
from flask import abort, redirect, url_for
from flask import render_template

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return login_post()
    else:
        return login_get()

def login_get():
    return render_template('login.html')

def login_post():
    class_name = request.form['class_name']
    places = request.form['places']
    error = "Недостаточно данных"
    return render_template('profile.html', class_name=class_name, places=places, error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=15000)