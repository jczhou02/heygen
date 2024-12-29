# Video Translation Client Library 
This project simulates a video translation server and a client library for interacting with it. 
## Features <br>
- A Flask-based server that transitions job status between `pending`, `completed`, and `error`. 
- A client library to interact with the server, using exponential backoff for efficient polling. - Integration tests for end-to-end testing.


## How to Use 
1. **Install Dependencies & Start the Server (powershell)** 
- Python 3.7 or higher
```pip install -r requirements.txt```
```python server/server.py```

2. **API / Endpoints** <br>
```GET /status``` <br>
```POST /start``` <br>  curl -X POST http://127.0.0.1:5000/start -H "Content-Type: application/json" -d "{\"delay\": 10}"
3. **Testing**<br>
I used pytest approach: <br>
```pip install pytest``` <br>
```python -m pytest tests/test.py```<br>

--- 
### Bells and Whistles
- **Configurable Backoff Strategy:** Allow the user to set backoff parameters (e.g., jitter). 
- **Logging:** Use Python's `logging` module to provide debug logs. 
- **Retry Logic:** Retry on transient errors like HTTP 500 or connection timeouts. 
- **Packaging:** Add a `setup.py` to make the client library installable via pip. 
---
### Debug Testing
#### Server Delay:
Your server takes 5 or 10 seconds to transition from pending to completed/error.
If for instance, the client library only retries max_retries=3, this may not cover the time required for the server to transition to a final state. <br>
Client Configuration: <br>
With init_delay=1 and exponential backoff (delay *= 2), the retry intervals are: 1s, 2s, 4s, for a total of 7 seconds before exhausting retries. This isn’t enough time for the server to complete its transition for delays like 5 or 10.
#### Solution
To fix this, you can either:
Increase the max_retries in your test to account for longer server delays.
Adjust the init_delay and max_delay values to cover the server delay while keeping retries reasonable.





