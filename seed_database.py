import os
import json
from random import choice, randint

import crud
import model
import server

os.system('dropdb edvid')
os.system('createdb edvid')
model.connect_to_db(server.app, 'postgresql:///edvid', echo=False)
model.db.create_all()

# Load movie data from JSON file
with open('videos.json') as f:
    video_data = json.loads(f.read())

# Create videos, store them in list so we can use them
# to create fake activities
videos_in_db = []

for video in video_data:
    link, title, notes = (video['link'],
                                    video['title'],
                                    video['notes'])

    db_video = crud.create_video(link,
                                 title,
                                 notes)
    videos_in_db.append(db_video)

# Create 10 users; each user will link to 3 videos
for n in range(10):
    email = f'user{n}@test.com'  # Voila! A unique email!
    password = 'test'

    user = crud.create_user(email, password)

    for x in range(3):
        random_video = choice(videos_in_db)
        #grade = randint(1, 6)
        fake_title = f'activity{x}'
        activity = crud.create_activity(fake_title, user)
        vidact = crud.create_association(random_video, activity)