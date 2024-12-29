import time
import requests
import logging

logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
class PollingTimeoutError(Exception):
    pass
class ServerResponseError(Exception):
    pass

class Client:
    def __init__(self, baseURL, init_delay=1, max_delay=16, max_retries=10):
        self.baseURL = baseURL
        self.init_delay = init_delay
        self.max_delay = max_delay
        self.max_retries = max_retries

    def poll_status(self):
        delay = self.init_delay
        for i in range(self.max_retries):
            try: 
                response = requests.get(self.baseURL + '/status', timeout=5)
                response.raise_for_status()  # raise an exception in case of http errors
                result = response.json().get('result')

                logging.info(f'Attempt {i+1}: Status = {result}')

                if result in ['completed', 'error']:
                    return result
                
            except requests.exceptions.RequestException as e:
                logging.error(f'Attempt {i+1}: {e}')
                if i == self.max_retries - 1:   # last attempt
                    raise PollingTimeoutError(f"Failed to fetch status after {self.max_retries} attempts")
            time.sleep(delay)
            delay = min(2*delay, self.max_delay)  # exponential backoff => the delay time will be doubled after each attempt
        raise PollingTimeoutError('Max retries exceeded w/o result')