from flask import Flask, request, jsonify
import time
import threading
import random

app = Flask(__name__)
status = {'result': 'pending'}
completed_time = None
error_p = 0.1

def sim_status(delay):
    global status
    global completed_time
    time.sleep(delay)
    if error_p > 0 and random.random() < error_p:
        status['result'] = 'error'
    else:
        status['result'] = 'completed'
    completed_time = time.time()

@app.route('/')
def home():
    return 'Weclome to the translation server!'

@app.route('/status', methods=['GET'])
def get_status():
    return jsonify(status)

@app.route('/start', methods=['POST'])
def start():
    global status
    global completed_time

    print("Incoming request data: ", request.json)
    print("Incoming JSON: ", request.json)
    if not request.json:
        return jsonify({'error': 'Invald JSON payload'}), 400

    status['result'] = 'pending'
    completed_time = None
    delay = request.json.get('delay', 10)   #  default delay is 10 seconds
    threading.Thread(target=sim_status, args=(delay,)).start()
    return jsonify({'message': 'Server started'})

if __name__ == '__main__':
    app.run(debug=True)