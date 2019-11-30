from flask import render_template,url_for,redirect,request,flash,abort
import os
import secrets
from app import app,db
from app.main.forms import UpdateAccountForm,PostForm
from app.models import Post,Clap,Comment
from app.requests import getQuotes
from . import main
from flask_login import login_required,current_user


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