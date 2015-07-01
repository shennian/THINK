import requests
from xml.dom import minidom
from Tkinter import *

# parse xml
xmldoc = minidom.parse('data.xml')
temperatures_xml = xmldoc.getElementsByTagName('temperature')
times_xml = xmldoc.getElementsByTagName('time')


times_list = []
temperatures_list = []
for i in range(len(temperatures_xml)):
    time_from = times_xml[i].attributes['from'].value
    time_to = times_xml[i].attributes['to'].value
    temperature = float(temperatures_xml[i].attributes['value'].value)
    times_list.append((time_from, time_to))
    temperatures_list.append(temperature)

# get data
max_temperature = temperatures_list[0]
min_temperature = temperatures_list[1]
if max_temperature < min_temperature:
    max_temperature, min_temperature = min_temperature ,max_temperature

for i in range(2, len(temperatures_list)):
    if temperatures_list[i] > max_temperature:
        max_temperature = temperatures_list[i]
    elif temperatures_list[i] < min_temperature:
        min_temperature = temperatures_list[i]

d_temperature = max_temperature - min_temperature
dy = 200 / d_temperature
# draw
master = Tk()

w = Canvas(master, width=800, height=400, background='white')

w.pack()


for i in range(1, 9):
    begin_x = 100 * (i - 1)
    begin_y = 350 - (temperatures_list[i-1] - min_temperature) * dy
    end_x = 100 * i
    end_y = 350 - (temperatures_list[i] - min_temperature) * dy
    w.create_line(begin_x, begin_y, end_x, end_y, fill='#FFCC00',width=3)

    k = float((end_y - begin_y) / (end_x - begin_x))
    for j in range(begin_x, end_x):
        #k = float((end_y - begin_y) / (end_x - begin_x))
        #print k
        y = k * (j - begin_x) + begin_y
        w.create_line(j, y+3, j, 350, fill='#FFFFAA')
    w.create_text((begin_x + end_x) / 2, (end_y + begin_y) / 2 - 20,
                                            text=temperatures_list[i-1])
    w.create_text((begin_x + end_x) / 2, 380 ,text=times_list[i][0][11: 16])
    #FFFF96

mainloop()
