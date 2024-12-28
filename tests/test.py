import subprocess
import requests
import time
from client.client import Client

def test_client():
    server = subprocess.Popen(['python', 'server/server.py'])
    time.sleep(2)
    
    try:
        requests.post('http://localhost:5000/start', json={'delay': 5})
        client = Client('http://localhost:5000')
        result = client.poll_status()
        print(f'Final result: {result}')
    finally:
        server.terminate()