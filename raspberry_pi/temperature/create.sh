#!/bin/bash

RRD_BASE="/home/pi/python/python_bot/raspberry_pi/temperature/temp.rrd"

rrdtool create $RRD_BASE --step 300 \
                          DS:ds0:GAUGE:600:U:U \
                          DS:ds1:GAUGE:600:U:U \
                          RRA:AVERAGE:0.5:1:8640 \
                          RRA:AVERAGE:0.5:3:2880 \
                          RRA:AVERAGE:0.5:6:1440 \
                          RRA:AVERAGE:0.5:12:720 \
                          RRA:MIN:0.5:1:8640 \
                          RRA:MIN:0.5:3:2880 \
                          RRA:MIN:0.5:6:1440 \
                          RRA:MIN:0.5:12:720 \
                          RRA:MAX:0.5:1:8640 \
                          RRA:MAX:0.5:3:2880 \
                          RRA:MAX:0.5:6:1440 \
                          RRA:MAX:0.5:12:720

exit 0
