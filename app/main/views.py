from flask import render_template
from . import main
from flask_login import login_required
@main.route('/')
def index():
    '''
    view root page function that returns index and its data
    '''
    return render_template('index.html')