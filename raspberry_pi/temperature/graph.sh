#!/bin/bash

RRD_BASE="/home/pi/python/python_bot/raspberry_pi/temperature/temp.rrd"
DATE="`date '+%d-%m-%Y %H\:%M\:%S'`"

rrdtool graph "/home/pi/python/python_bot/raspberry_pi/temperature/temp_1d.png" \
              --start -1d \
              --end now \
              --imgformat PNG \
              --width=700 --height=250 \
              --title "Температура (C)" \
              --font TITLE:12:Arial \
              --slope-mode \
              --alt-autoscale \
              DEF:data_source0=$RRD_BASE:ds0:AVERAGE \
              DEF:data_source1=$RRD_BASE:ds1:AVERAGE \
              TEXTALIGN:center \
              LINE2:data_source0#FF0000:"В комнате\t" \
              GPRINT:data_source0:LAST:" Current\: %2.2lf %s" \
              GPRINT:data_source0:MIN:"Min\: %2.2lf %s" \
              GPRINT:data_source0:MAX:"Max\: %2.2lf %s" \
              GPRINT:data_source0:AVERAGE:"Avg\: %2.2lf %s" \
              LINE2:data_source1#24BC14:"На улице\t\r" \
              GPRINT:data_source1:LAST:" Current\: %2.2lf %s" \
              GPRINT:data_source1:MIN:"Min\: %2.2lf %s" \
              GPRINT:data_source1:MAX:"Max\: %2.2lf %s" \
              GPRINT:data_source1:AVERAGE:"Avg\: %2.2lf %s" \
              COMMENT:"\r" \
              COMMENT:"Последнее обновление\: $DATE\l" \
              > /dev/null 2>&1
exit 0
