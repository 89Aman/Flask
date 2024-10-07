from flask import Flask, render_template, redirect, url_for, request, session, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

# A simple user dictionary for demonstration purposes (You can replace this with a database)
users = {
    "user1": "password1",
    "user2": "password2"
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the user exists and the password matches
        if username in users and users[username] == password:
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'danger')

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return f'Welcome {session["username"]}! You are logged in. <a href="/logout">Logout</a>'
    else:
        flash('You need to login first', 'warning')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
