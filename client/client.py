import time
import requests

class Client:
    def __init__(self, baseURL):
        self.baseURL = baseURL

    def poll_status(self, max_retries=10, init_delay=1, max_delay=16):
        delay = init_delay
        for i in range(max_retries):
            response = requests.get(self.baseURL + '/status')
            if response.status_code != 200:
                raise Exception('Failed to fetch status')
            result = response.json().get('result')
            print(f'Attempt {i+1}: Status = {result}')
            if result in ['completed', 'error']:
                return result
            time.sleep(delay)
            delay = min(2*delay, max_delay)  # exponential backoff => the delay time will be doubled after each attempt
        raise TimeoutError('Max retries exceeded w/o result')