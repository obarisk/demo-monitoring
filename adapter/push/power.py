#!/usr/bin/env python3

"""
-s sensor_id -c connection_string -i interval seconds (must > 1)
"""

import os
import random
import sys
import time
import psycopg

cmd_temphum   = os.path.dirname(os.path.abspath(__file__)) + "/../../simulator/temphum.py"
conn_string   = sys.argv[4]
push_interval = int(sys.argv[6])

def cumulative(c, interval) -> float:
    if random.binomialvariate(1, 0.2) >= 1:
        v = round(random.normalvariate(2500, 50), 2)
    else:
        v = round(random.normalvariate(2000, 20), 2)
    c += round(v / 3600 * interval, 2)
    if c > 1000000:
        c -= 1000000
    return round(c, 2)

def current(conn, sensor_id):
    with conn.cursor() as cursor:
        res = cursor.execute(
            f"SELECT COALESCE(MAX(v), 0) FROM records WHERE s = {sensor_id} AND l = 3")
        rec = res.fetchall()[0]
    return float(rec[0])

def push(conn, id, record):
    sql = (
      "INSERT INTO records (t, s, l, v) VALUES "
      f"(now(), {id}, 3, {record})"
    )
    with conn.cursor() as cursor:
        cursor.execute(sql)
    conn.commit()

if __name__ == "__main__":
    conn = psycopg.connect(conn_string)
    value = current(conn, sys.argv[2])
    latest = int(time.time()) - push_interval
    while True:
        if time.time() - latest > push_interval:
            value = cumulative(value, push_interval)
            push(conn, sys.argv[2], value)
            latest = int(time.time())
            print(f"{time.strftime('%Y-%m-%d %H:%M:%S')}: {value}")
        time.sleep(1)
