from flask import render_template,redirect,url_for,abort
from app.auth.views import login
from . import main 
from flask_login import current_user,login_required
from ..models import Pitch,User,Comment
from .forms import PitchForm,CommentForm
# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')
@main.route('/pitch')
def pitch():

    '''
    View root page function that returns the index page and its data
    '''
    pitches = Pitch.query.all()
    return render_template('pitch.html', pitch = pitches)

@main.route('/create_new', methods = ['POST','GET'])
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        category = form.category.data
        new_pitch_object = Pitch(post=post,category=category,title=title)
        new_pitch_object.save_p()
        return redirect(url_for('main.pitch'))
        
    return render_template('create_pitch.html', form = form)


@main.route('/comment/<int:pitch_id>', methods = ['POST','GET'])
@login_required
def comment(pitch_id):
    form = CommentForm()
    pitch = Pitch.query.get(pitch_id)
    all_comments = Comment.query.filter_by(pitch_id = pitch_id).all()
    if form.validate_on_submit():
        comment = form.comment.data 
        pitch_id = pitch_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(comment = comment,user_id = user_id,pitch_id = pitch_id)
        new_comment.save_c()
        return redirect(url_for('.comment', pitch_id = pitch_id))
    return render_template('comment.html', form =form, pitch = pitch,all_comments=all_comments)


@main.route('/user/<name>')
def profile(name):
    user = User.query.filter_by(username = name).first()
    user_id = current_user._get_current_object().id
    posts = Pitch.query.filter_by(user_id = user_id).all()
    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user,posts=posts)
