from flask import render_template, request, redirect, url_for, flash, session
from . import users_bp

@users_bp.route('/hi/<string:name>')
def greetings(name):
    name = name.upper()
    age = request.args.get('age', None, int)

    return render_template('users/hi.html', name = name, age = age)

@users_bp.route('/admin')
def admin():
    to_url = url_for('users.greetings', name='administrator', age=45, _external=True)
    print(to_url)    
    return redirect(to_url)

@users_bp.route('/login', methods=['GET', 'POST'])
def login():
    testUsername = 'user'
    testPassword = 'password'

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == testUsername and password == testPassword:
            session['user'] = username

            flash('Login successful', 'success')
            
            return redirect(url_for('users.profile'))

        flash('Invalid username or password', 'danger')
        return redirect(url_for('users.login'))

    return render_template('users/login.html')

@users_bp.route('/profile')
def profile():
    if 'user' not in session:
        flash('Please login first', 'danger')
        return redirect(url_for('users.login')) 
    
    username = session['user']

    return render_template('users/profile.html', username = username)

@users_bp.route('/logout')
def logout():
    session.pop('user', None)
    flash('You have been logged out', 'success')
    return redirect(url_for('users.login'))
