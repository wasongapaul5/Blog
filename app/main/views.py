import os
import secrets

from PIL import Image
from flask import render_template, url_for, redirect, request, flash, abort
from flask_login import current_user, login_required

from . import app
from app import db
from app.main import main
from app.main.forms import UpdateAccountForm, PostForm
from app.models import Post, Clap, Comment
from app.requests import getQuotes


@main.route('/')
@main.route('/home')
def index():
    '''
    view root page function that returns index and its data
    '''
    quotes = getQuotes()
    posts = Post.query.all()
    return render_template('index.html',quotes=quotes, posts=posts, current_user=current_user)

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_path = os.path.join(app.root_path, 'static/profile_pic', picture_fn)

    output_size = (125,125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

@main.route('/profile',methods=['GET','POST'])
@login_required
def profile():
    form = UpdateAccountForm()
    if form.picture.data:
        picture_file = save_picture(form.picture.data)
        current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated successfully!')
        return redirect(url_for('main.profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        image_file = url_for('static',filename='profile_pic/' + current_user.image_file)
        return render_template('profile/profile.html',title='Profile', imag_file=image_file,form=form)
        