"""
-p 8080 -t mean -h humidity -w watts_per_second

requirement:
pip install -U prometheus_client
"""

import sys
import time
import random
from prometheus_client import start_http_server, Gauge, Counter

update_interval = 10

metrics = {
    "temperature": Gauge(
      "temperature_celsius",
      "Temperature in Celsius",
    ),
    "humidity": Gauge(
      "humidity_percentage",
      "Humidity in percentage",
    ),
    "power": Counter(
      "power_consumption_watts",
      "Power consumption in Watts",
    )
}

def get_argument() -> dict:
  arguments = {
    4: 30.0,
    6: 40.0,
    8: 0.5,
  }
  for idx, arg in enumerate(sys.argv):
    match idx:
      case 2 | 4 | 6:
        try:
          v = float(arg)
          arguments[idx] = v
        except Exception as e:
          print(e)
  arguments[6] = arguments[6] * update_interval
  return arguments

def update(arg: dict) -> None:
  if random.binomialvariate(1, 0.01) >= 1:
    metrics["temperature"].set(round(arg[2] * 2 + random.normalvariate(0, 5), 2))
    metrics["humidity"].set(round(arg[4] * 2 + random.normalvariate(0, 5), 2))
    metrics["power"].inc(arg[6] * 2 + random.normalvariate(0, 0.1))
  else:
    metrics["temperature"].set(round(arg[2] + random.normalvariate(0, 2), 2))
    metrics["humidity"].set(round(arg[4] + random.normalvariate(0, 2), 2))
    metrics["power"].inc(arg[6] + random.normalvariate(0, 0.05))

def main():
  arg = get_argument()
  port = int(sys.argv[2])
  start_http_server(port)
  print(f"servering on port {port}")
  # # FIXME: fetch sensor data
  try:
    while True:
      update(arg)
      time.sleep(update_interval)
  except KeyboardInterrupt:
    print("stop")

if __name__ == "__main__":
  main()