#!/usr/bin/env ash

python app/exporter.py -p 8081 -t 20 -h 20 -p 0.1 &
python app/exporter.py -p 8082 -t 20 -h 20 -p 0.2 &
python app/exporter.py -p 8083 -t 20 -h 20 -p 0.3 &
python app/exporter.py -p 8084 -t 20 -h 20 -p 0.4 &
python app/exporter.py -p 8085 -t 40 -h 20 -p 1.0 &
python app/exporter.py -p 8086 -t 40 -h 20 -p 1.0 &
python app/exporter.py -p 8087 -t 40 -h 20 -p 1.0 &
python app/exporter.py -p 8088 -t 40 -h 20 -p 1.0 &
python app/exporter.py -p 8089 -t 60 -h 40 -p 2.0 &
python app/exporter.py -p 8090 -t 60 -h 40 -p 2.0 &
python app/exporter.py -p 8091 -t 60 -h 40 -p 4.0 &
python app/exporter.py -p 8092 -t 60 -h 40 -p 4.0 &
python app/exporter.py -p 8093 -t 60 -h 40 -p 2.0 &
python app/exporter.py -p 8094 -t 60 -h 40 -p 2.0 &

while true
do
  date
  sleep 30
done