from flask import render_template,url_for,redirect,flash,request
from flask_login import login_user,logout_user,current_user
from app.auth import auth
from app.auth.forms import LoginForm,RegisterForm
from app.models import User
from ..email import mail_message

@auth.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            next_url = request.args.get('next')
            return redirect(next_url) if next_url else redirect(url_for('main.index'))
        else:
            flash('Unsuccessful Login.Please  confirm your email and password details', 'danger')
        return render_template('auth/login.html', title='Login', form=form)

    
