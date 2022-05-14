import requests
from flask import Flask
from flask import render_template, request, flash, jsonify
from datetime import date, timedelta


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

API_KEY = '2vQAcXAiH93sXDdxdeLP1vOEMgQITMLHwbJiHWqN'


@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/apod-api', methods=['GET', 'POST'])
def apod():
    if request.method == 'POST':
        endpoint = 'https://api.nasa.gov/planetary/apod'

        d = request.form.get('date')

        parameters = {'api_key': API_KEY, 'date': d}
        response = requests.get(endpoint, params=parameters)
        info = response.json()
        return jsonify({'success': 'facts', 'info': info})

    today = date.today()
    endpoint = 'https://api.nasa.gov/planetary/apod'

    d = request.form.get('date')
    if not d:
        d = today - timedelta(days=1)
    parameters = {'api_key': API_KEY, 'date': d}
    response = requests.get(endpoint, params=parameters)

    info = response.json()
    return render_template('apod.html', today=today, info=info)


@app.route('/mars-rover-photos', methods=['GET', 'POST'])
def mars_rover():
    today = date.today()
    endpoint = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?'
    d = request.form.get('earth_date')
    if not d:
        d = today - timedelta(days=1)
    parameters = {'api_key': API_KEY, 'earth_date': d}
    response = requests.get(endpoint, params=parameters)
    info = response.json()['photos']
    if not info:
        flash('No photos available for that day', category='error')

    return render_template('mars_rover.html', info=info, today=today)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
