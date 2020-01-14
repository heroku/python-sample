import os
from flask import Flask
import time

app = Flask(__name__)

hogwarts_students =[
    {
        "id": 0,
        "first_name": "Harry",
        "last_name": "Potter",
        "creation_time": time.strftime("%H:%M:%S", time.gmtime()),
        "last_update_time": "",
        "magic_skills": {
            "Alchemy": "4",
            "Illusion": "3",
            "Summoning": "3",
            "Invisibilty": "4",
        },
        "desired_skills": {
            "Summoning": "5",
            "Invulnerability": "1",
            "Omnipresent": "1",
            "Invisibility": "5"
        },
        "desired_course": "Alchemy advanced"

    },
    {
        "id": 1,
        "first_name": "Ron",
        "last_name": "Weasley",
        "creation_time": time.strftime("%H:%M:%S", time.gmtime()),
        "last_update_time": "",
        "magic_skills": {
            "Alchemy": "3",
            "Animation": "3",
            "Healing": "3",
            "Invisibility": "2",
        },
        "desired_skills": {
            "Summoning": "1",
            "Invulnerability": "2",
            "Illusion": "1",
            "Invisibility": "3"
        },
        "desired_course": "Dating with Magic"
    }
]

@app.route("/")
def index():
    return str(hogwarts_students)


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)