'''
Sensehat Dashboard
--------------------
Author: drdynscript
Modified: 03-12-2019
--------------------
Installation:
sudo pip3 -U Flask
Docs: http://flask.pocoo.org/docs/1.0/
'''
# Import the libraries
from flask import Flask, jsonify, render_template, request
from sense_hat import SenseHat

# Create an instance of flask
app = Flask(__name__)

# Create an instance of the sensehat
sense = SenseHat()

# Define the root route
@app.route('/')
def index():
  return 'Look the flask server is running'

# Define the nmd route
@app.route('/nmd')
def nmd():
  return 'Greetings Earthlings. We are NMDrs'

# Define the my_ip route
@app.route('/my_ip', methods=['GET'])
def my_ip():
  return jsonify({
    'ip': request.remote_addr
  }), 200

# Define the api_environment route
@app.route('/api/environment', methods=['GET'])
def api_environment():
  environment_obj = {
    'temperature': {
      'value': round(sense.get_temperature()),
      'unit': u'C'
    },
    'humidity': {
      'value': round(sense.get_humidity()),
      'unit': u'%'
    },
    'pressure': {
      'value': round(sense.get_pressure()),
      'unit': u'mbar'
    }
  }
  return jsonify(environment_obj), 200

# Define the api_environment route
@app.route('/environment', methods=['GET'])
def environment():
  environment_obj = {
    'temperature': {
      'value': round(sense.get_temperature()),
      'unit': u'°C'
    },
    'humidity': {
      'value': round(sense.get_humidity()),
      'unit': u'%'
    },
    'pressure': {
      'value': round(sense.get_pressure()),
      'unit': u'mbar'
    }
  }
  return render_template('environment.html', environment=environment_obj)

# Main method for Flask server
if __name__ == '__main__':
  app.run(host = '10.5.129.26', port = 8080, debug = True)