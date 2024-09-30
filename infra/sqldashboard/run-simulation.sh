#!/usr/bin/env bash

python3 /home/u/demo-monitoring/adapter/push/power.py   -s 1 -c "postgres://postgres:password@127.0.0.1:5432/postgres" -i 30 &
python3 /home/u/demo-monitoring/adapter/push/temphum.py -s 1 -c "postgres://postgres:password@127.0.0.1:5432/postgres" -i 30 &

python3 /home/u/demo-monitoring/adapter/push/power.py   -s 2 -c "postgres://postgres:password@127.0.0.1:5432/postgres" -i 45 &
python3 /home/u/demo-monitoring/adapter/push/temphum.py -s 2 -c "postgres://postgres:password@127.0.0.1:5432/postgres" -i 45 &

python3 /home/u/demo-monitoring/adapter/push/power.py   -s 3 -c "postgres://postgres:password@127.0.0.1:5432/postgres" -i 60 &
python3 /home/u/demo-monitoring/adapter/push/temphum.py -s 3 -c "postgres://postgres:password@127.0.0.1:5432/postgres" -i 60 &

python3 /home/u/demo-monitoring/adapter/push/power.py   -s 11 -c "postgres://postgres:password@127.0.0.1:5432/postgres" -i 30 &
python3 /home/u/demo-monitoring/adapter/push/temphum.py -s 11 -c "postgres://postgres:password@127.0.0.1:5432/postgres" -i 30 &

python3 /home/u/demo-monitoring/adapter/push/power.py   -s 12 -c "postgres://postgres:password@127.0.0.1:5432/postgres" -i 45 &
python3 /home/u/demo-monitoring/adapter/push/temphum.py -s 12 -c "postgres://postgres:password@127.0.0.1:5432/postgres" -i 45 &

python3 /home/u/demo-monitoring/adapter/push/power.py   -s 13 -c "postgres://postgres:password@127.0.0.1:5432/postgres" -i 60 &
python3 /home/u/demo-monitoring/adapter/push/temphum.py -s 13 -c "postgres://postgres:password@127.0.0.1:5432/postgres" -i 60 &

python3 /home/u/demo-monitoring/adapter/push/power.py   -s 33 -c "postgres://postgres:password@127.0.0.1:5432/postgres" -i 30 &
python3 /home/u/demo-monitoring/adapter/push/temphum.py -s 33 -c "postgres://postgres:password@127.0.0.1:5432/postgres" -i 30 &

python3 /home/u/demo-monitoring/adapter/push/power.py   -s 32 -c "postgres://postgres:password@127.0.0.1:5432/postgres" -i 45 &
python3 /home/u/demo-monitoring/adapter/push/temphum.py -s 32 -c "postgres://postgres:password@127.0.0.1:5432/postgres" -i 45 &

python3 /home/u/demo-monitoring/adapter/push/power.py   -s 31 -c "postgres://postgres:password@127.0.0.1:5432/postgres" -i 60 &
python3 /home/u/demo-monitoring/adapter/push/temphum.py -s 31 -c "postgres://postgres:password@127.0.0.1:5432/postgres" -i 60 &
