#!/usr/bin/env python3

"""
-s sensor_id -c connection_string -i interval seconds (must > 1)

on windown
pip install psycopg[binary]
"""

import os
import subprocess
import sys
import time
import platform
import psycopg

cmd_temphum   = os.path.dirname(os.path.abspath(__file__)) + "/../../simulator/temphum.py"
if platform.system() == "Windows":
    cmd_temphum = ["python", cmd_temphum]
else:
    cmd_temphum = [cmd_temphum]
conn_string   = sys.argv[4]
push_interval = int(sys.argv[6])

def capture():
    global cmd_temphum
    output = subprocess.run(cmd_temphum, capture_output=True)
    return output.stdout.decode().strip()

def parser(txt):
    l = txt.split()
    return {
      "temperature": float(l[6].replace("C", "")),
      "humidity": float(l[8].replace("%", ""))
    }

def push(conn, id, record):
    sql = (
      "INSERT INTO records (t, s, l, v) VALUES "
      f"(now(), {id}, 1, {record['temperature']}),"
      f"(now(), {id}, 2, {record['humidity']})"
    )
    with conn.cursor() as cursor:
        cursor.execute(sql)
    conn.commit()

if __name__ == "__main__":
    conn = psycopg.connect(conn_string)
    latest = int(time.time()) - push_interval
    while True:
        if time.time() - latest > push_interval:
            value = parser(capture())
            push(conn, sys.argv[2], value)
            latest = int(time.time())
            print(f"{time.strftime('%Y-%m-%d %H:%M:%S')}: {value}")
        time.sleep(1)