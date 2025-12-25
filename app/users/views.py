from flask import render_template, request, redirect, url_for, flash, session, make_response
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

@users_bp.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'user' not in session:
        flash('Please login first', 'danger')
        return redirect(url_for('users.login'))

    username = session['user']

    if request.method == 'POST':
        action = request.form.get('action')
        response = redirect(url_for('users.profile'))
        
        if action == 'add':
            key = request.form.get('key')
            value = request.form.get('value')
            max_age = request.form.get('max_age')

            if not key:
                flash("Введіть ключ для кукі", "danger")
                return response

            response.set_cookie(
                key,
                value = str(value) if value else "",
                max_age=int(max_age) if max_age else None
            )
            flash(f"Cookie '{key}' успішно додано", 'success')
            return response

        elif action == 'delete_one':
            key = request.form.get('key')

            if not key:
                flash("Введіть ключ для кукі", "danger")
                return response
            
            if key in request.cookies:
                response.delete_cookie(key)
                flash(f"Cookie '{key}' видалено", 'success')
                return response
            else:
                flash(f"Cookie '{key}' не знайдено", 'warning')
                return response

        elif action == 'delete_all':
            for key in request.cookies.keys():
                if key != 'session': 
                    response.delete_cookie(key)
            flash("Всі cookie видалено", 'success')
            return response

    return render_template("users/profile.html", username=username, cookies=request.cookies)
    
@users_bp.route('/logout')
def logout():
    session.pop('user', None)
    flash('You have been logged out', 'success')
    return redirect(url_for('users.login'))
