"""Server for educational videos app."""

from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db
from pprint import pformat
import crud
import os

app = Flask(__name__)
app.secret_key = 'SECRETSECRETSECRET'

# This configuration option makes the Flask interactive debugger
# more useful (you should remove this line in production though)
app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = True


#API_KEY = os.environ['API_KEY']


@app.route('/')
def start_here():
    """Homepage."""
    return render_template("index.html")


# Temporary page, to ensure video list loads.
@app.route('/videos')
def get_videos():
    """Display all videos."""

    videos = crud.get_all_vids()
    return render_template("all_videos.html", videos=videos)


# Temporary page, to ensure video data is accessed and can be displayed properly.
@app.route('/videos/<video_id>')
def show_movie_details(video_id):
    """Show details on a particular video."""
    
    video = crud.get_video_by_id(video_id)
    return render_template("video_details.html", video = video)

@app.route('/movies')
def display_movies():
    """View a list of all movies with links."""

    movies = crud.get_movies()
    
    return render_template('all_movies.html', movies = movies)


@app.route('/movies/<movie_id>')
def display_this_movie(movie_id):
    """Show details of a particular movie."""

    movie = crud.get_movie_by_id(movie_id)
    
    return render_template('movie_details.html', movie = movie)


@app.route('/users')
def display_all_users():
    """View a list of all users with option to rate movies."""

    users = crud.get_users()
    
    return render_template('all_users.html', users = users)


@app.route('/users/<user_id>')
def display_this_user(user_id):
    """Show details for a particular user."""

    user = crud.get_user_by_id(user_id)
    
    return render_template('user_details.html', user = user)


@app.route('/users', methods=['POST'])
def register_user():
    """Create a new user."""

    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)

    if user:
        flash('Cannot create an account with that email. Try again.')
    else: 
        user = crud.create_user(email, password)
        flash('Account created! Please log in.')
    
    return redirect('/')

if __name__ == '__main__':
    connect_to_db(app, 'postgresql:///edvid', echo=False) # Does this go here?
    app.run(host='0.0.0.0', debug=True)

