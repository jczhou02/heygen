import subprocess
import requests
import time
from client.client import Client
import pytest

def test_client():
    server = subprocess.Popen(['python', 'server/server.py'])
    time.sleep(2)
    
    try:
        response = requests.post('http://127.0.0.1:5000/start', json={'delay': 5})
        print('Start response:', response.json())

        client = Client(baseURL='http://127.0.0.1:5000', init_delay=1, max_delay=16, max_retries=5)
        result = client.poll_status()
        print(f'Final result: {result}')

    finally:
        server.terminate()
        server.wait()

@pytest.mark.parametrize('delay', [3, 5, 10])
def test_client_with_params(delay):
    server = subprocess.Popen(['python', 'server/server.py'])
    time.sleep(2)
    
    try:
        response = requests.post('http://127.0.0.1:5000/start', json={'delay': delay})
        assert response.status_code == 200
        print(f'Start response for delay {delay}:', response.json())

        max_retries = delay // 2 + 2  
        client = Client(baseURL='http://127.0.0.1:5000', init_delay=1, max_delay=16, max_retries=max_retries)
        result = client.poll_status()
        
        assert result in ['completed', 'error']
        print(f'Final result for delay {delay}: {result}')
    
    finally:
        server.terminate()
        server.wait()