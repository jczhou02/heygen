import subprocess
import requests
import time
from client.client import Client

def test_client():
    server = subprocess.Popen(['python', 'server/server.py'])
    time.sleep(2)
    
    try:
        response = requests.post('http://127.0.0.1:5000/start', json={'delay': 5})
        print('Start response:', response.json())

        client = Client('http://127.0.0.1:5000')
        result = client.poll_status()
        print(f'Final result: {result}')
    finally:
        server.terminate()