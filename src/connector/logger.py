import json
import random
from time import sleep

class LoggerConnector:
  def send(self, message=None, **kwargs):
    # mock sevire API latency
    sleep(random.randint(5,10))

    if message:
      kwargs['message'] = message

    print(f"wrote event: {json.dumps(kwargs)}")