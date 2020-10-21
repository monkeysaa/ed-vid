"""Models for educational videos app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    # activities = a list of Activity objects

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'


class Activity(db.Model):
    """An educational activity."""

    __tablename__ = 'activities'

    activity_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    user = db.relationship('User', backref='activities')

    # edvid_associations = a list of VidActivity objects

    def __repr__(self):
        return f'<Activity activity_id={self.activity_id} title={self.title}>'


class Video(db.Model):
    """A favorite video."""

    __tablename__ = 'videos'

    video_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    link = db.Column(db.String, nullable=False)
    title = db.Column(db.String)
    # add video length
    notes = db.Column(db.Text)

    # edvid_associations = a list of VidActivity objects

    def __repr__(self):
        return f'<Video video_id={self.video_id} title={self.title}>'


class VidActivity(db.Model):
    """An educational video-activity association."""

    __tablename__ = 'edvid_associations' # should I redo to remove hyphen? 
    # remember these sql queries need to read "edvid_associations"

    vidAct_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    video_id = db.Column(db.Integer, db.ForeignKey('videos.video_id'))
    activity_id = db.Column(db.Integer, db.ForeignKey('activities.activity_id'))

    video = db.relationship('Video', backref='edvid_associations')
    activity = db.relationship('Activity', backref='edvid_associations')

    def __repr__(self):
        return f'<VidActivity vidAct_id={self.vidAct_id}>'
    

def connect_to_db(flask_app, db_uri, echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    # the line below tells SQLAlchemy not to print every query it executes.
    
    connect_to_db(app, 'postgresql:///edvid', echo=False)  


# N.B. - Figure out how to add in subject & grade once framework works.  
# how do I store in a way that's searchable and filter-able?
# subject = db.Column(db.String)
# grade_level = db.Column(db.String)
