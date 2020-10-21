"""CRUD operations for educational videos app."""

from model import db, User, Video, Activity, VidActivity, connect_to_db

             
def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def create_activity(title, user): # pass grade and subject here...
    """Create and return a new movie."""

    activity = Activity(title = title, user = user)

    db.session.add(activity)
    db.session.commit()

    return activity

def create_video(link, title, notes = ""):
    """Create and return a video."""

    video = Video(link = link, title = title, notes = notes)

    db.session.add(video)
    db.session.commit()

    return video

#Consider deleting later
def get_all_vids():
    """Return a list of all videos.""" 

    return Video.query.all()

#Consider deleting later
def get_video_by_id(video_id):
    """Return a video object.""" 

    return Video.query.get(video_id)


def create_association(video, activity):
    """Create and return an association."""

    association = VidActivity(video = video, activity = activity)

    db.session.add(association)
    db.session.commit()
    
# Do I need to return something here?
    return association