import os
home_dir = '/home/pi/python/python_bot/raspberry_pi/temperature/'
temp_home_file = open("/sys/bus/w1/devices/28-a8753c126461/temperature")
temp_home_data = temp_home_file.readlines()
temp_home_file.close()
temperature = float(temp_home_data[0]) / 1000

temp_outside_file = open("/sys/bus/w1/devices/28-fdc577126461/temperature")
temp_outside_data = temp_outside_file.readlines()
temp_home_file.close()
temperature_outside = float(temp_outside_data[0]) / 1000

command = f"rrdtool update {home_dir}temp.rrd N:{temperature}:{temperature_outside}"
os.system(command)
os.system(f'{home_dir}graph.sh')
