from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from midiutil import MIDIFile
import datetime
import ephem
import numpy as np


app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_midi():
    try:
        birthdate_input = request.form['birthdate']
        birthday = datetime.datetime.strptime(birthdate_input, '%Y-%m-%d').date()
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."
    observer = ephem.Observer()
    observer.lat = '52.5200'  # Replace with the latitude of the location
    observer.long = '13.4050'  # Replace with the longitude of the location

    # Define celestial objects
    celestial_objects = {
        "Sun": ephem.Sun(),
        "Moon": ephem.Moon(),
        "Mercury": ephem.Mercury(),
        "Venus": ephem.Venus(),
        "Mars": ephem.Mars(),
        "Jupiter": ephem.Jupiter(),
        "Saturn": ephem.Saturn(),
        "Uranus": ephem.Uranus(),
        "Neptune": ephem.Neptune(),
        "Pluto": ephem.Pluto(),
        # Add more classical planets
    }

    # Create a MIDI composition
    midi = MIDIFile()

    # Simulate a year
    for frame in range(365):
        # Calculate the user's house placement (customize as needed)
        user_house = 1  # Example: assume the user's birthdate places them in the 1st house

        # Define tempo values for each house (customize as needed)
        house_tempos = {
            1: 120,
            2: 100,
            3: 90,
            4: 80,
            5: 110,
            6: 95,
            7: 115,
            8: 105,
            9: 125,
            10: 130,
            11: 85,
            12: 75,
            # Add tempo values for other houses
        }

        # Adjust the tempo based on the house (customize as needed)
        tempo = house_tempos[user_house]

        for celestial, celestial_object in celestial_objects.items():
            # Calculate the position of the celestial object for the current date
            celestial_object.compute(birthday + datetime.timedelta(days=frame))

            # Calculate the user's zodiac sign based on the Sun's position
            if celestial == "Sun":
                user_zodiac = ephem.constellation(celestial_object)[1]

            # Calculate the note based on the user's zodiac sign (customize as needed)
            zodiac_notes = {
                "Aries": 60,
                "Taurus": 62,
                "Gemini": 64,
                "Cancer": 65,
                "Leo": 67,
                "Virgo": 69,
                "Libra": 71,
                "Scorpius": 72,
                "Sagittarius": 74,
                "Capricornus": 76,
                "Aquarius": 77,
                "Pisces": 79,
                "Ophiuchus":81,
                # Add more zodiac notes
            }

            note = zodiac_notes[user_zodiac]
            time = frame
            duration = 1
            velocity = 100

            midi.addNote(0, 0, note, time, duration, velocity)

        # Set the tempo for the current frame
        midi.addTempo(0, frame, tempo)

    # Save the MIDI composition to a file
    with open('static/celestial_music.mid', 'wb') as output_file:
        midi.writeFile(output_file)

    # Create a MIDI composition and add notes

    # Save the MIDI composition to a file

    return send_from_directory('static', 'celestial_music.mid', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

