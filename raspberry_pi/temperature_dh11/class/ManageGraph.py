import os
import subprocess


class ManageGraph:
    current_dir = '/home/pi/python/python_bot/raspberry_pi/temperature_dh11'

    def __init__(self, g_name, g_data_source, rrd_data=None, g_start='1d'):
        self.g_dir = self.current_dir
        self.g_name = g_name
        self.g_start = g_start
        self.g_data_source = g_data_source
        self.rrd_data = rrd_data
        self.rrd_file = f"{self.g_dir}/{self.g_name}_{self.g_start}.rrd"
        self.graph_file = f"{self.g_dir}/{self.g_name}_{self.g_start}.png"
        self.create()
        self.update()

    def create(self):
        if not os.path.exists(self.rrd_file):
            data_source = ''
            for data in self.g_data_source:
                name = data.get('name')
                data_source = data_source + f'DS:{name}:GAUGE:600:U:U '
            template_graph = f'''
                rrdtool create {self.rrd_file} --step 300 \
                              {data_source} \
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
            '''
            subprocess.run(template_graph, shell=True)

    def update(self):
        if self.rrd_data:
            str_data = ''
            for data in self.rrd_data:
                str_data = str_data + f"{data}:"
            print(self.rrd_file)
            command = f"rrdtool update {self.rrd_file} N{str_data[:-1]}"
            subprocess.run(command, shell=True)

    def rrdtool_graph_update(self):
        data_source = ''
        for data in self.g_data_source:
            name = data.get('name')
            color = data.get('color')
            label = data.get('label')
            data_source = (data_source +
                           f'DEF:graf_{name}={self.rrd_file}:{name}:AVERAGE '
                           f'LINE2:graf_{name}#{color}:"{label}" '
                           f'GPRINT:graf_{name}:LAST:" Current\\: %2.2lf %s" '
                           f'GPRINT:graf_{name}:MIN:"Min\\: %2.2lf %s" '
                           f'GPRINT:graf_{name}:MAX:"Max\\: %2.2lf %s" '
                           f'GPRINT:graf_{name}:AVERAGE:"Avg\\: %2.2lf %s" '
                           )

        graph_data = (
                    f'rrdtool graph "{self.graph_file}" ' 
                    f'--start -1d '
                    f'--end now '
                    f'--imgformat PNG '
                    f'--width=700 '
                    f'--height=250 '
                    f'--title "Температура (C)" '
                    f'--font TITLE:12:Arial '
                    f'--slope-mode '
                    f'--alt-autoscale '
                    f'{data_source} '
                    # f'COMMENT:"" '
                    # f'COMMENT:"Последнее обновление\:\l" '
        )
        result = subprocess.run(graph_data, shell=True)
        print(result)

