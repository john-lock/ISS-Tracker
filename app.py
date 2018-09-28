from flask import Flask, render_template
import json
import os
import time
import requests


app = Flask(__name__)
apikey = os.environ['APIKEY']

@app.route('/', methods=['GET'])
def main():
    astro_data = None
    now_data = None
    errors = None

    # ISS NOW
    iss_now_url = "http://api.open-notify.org/iss-now.json"
    try:
        now_r = requests.get(iss_now_url)
    except requests.ConnectionError:
        errors = "ConnectionError"
    now_data = json.loads(now_r.text)
    lati = now_data['iss_position']['latitude']
    lon = now_data['iss_position']['longitude']

    # Timestamp
    raw_timestamp = now_data['timestamp']
    timestamp = time.ctime(raw_timestamp)

    # Astronaut data
    astros_url = 'http://api.open-notify.org/astros.json'
    try:
        r = requests.get(astros_url)
    except requests.ConnectionError:
        errors = "ConnectionError for Astros"
    astro_data = json.loads(r.text)
    astros = astro_data['people']
    iss_astros = [x for x in astros if x['craft'] == "ISS"]
    other_astros = [x for x in astros if x['craft'] != "ISS"]

    return render_template('index.html', lati=lati, lon=lon, now_data=now_data, apikey=apikey, errors=errors, iss_astros=iss_astros, other_astros=other_astros, timestamp=timestamp)


if __name__ == '__main__':
    app.run()
