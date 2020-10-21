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
    return render_template("homepage.html")


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


if __name__ == '__main__':
    connect_to_db(app, 'postgresql:///edvid', echo=False) # Does this go here?
    app.run(host='0.0.0.0', debug=True)

