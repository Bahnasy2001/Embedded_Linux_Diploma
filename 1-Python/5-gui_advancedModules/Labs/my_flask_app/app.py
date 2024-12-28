from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample user credentials
users = {"Hassan": "Hassan", "Bahnasy": "Bahnasy"}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Check if credentials are valid
        if username in users and users[username] == password:
            return redirect(url_for('dashboard', username=username))
        else:
            error = "Invalid credentials. Please try again."
    return render_template('login.html', error=error)

@app.route('/dashboard/<username>')
def dashboard(username):
    return render_template('dashboard.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
