import turtle
import requests
from xml.dom import minidom


# get xml data from api
r = requests.get('http://api.openweathermap.org/data/2.5/forecast?q=chongqing,cn&mode=xml')
fp = open('data.xml', 'w')
fp.write(r.text)
fp.close()

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


turtle.screensize(800,800)
turtle.setworldcoordinates(0, 0, 800,800)

tess = turtle.Turtle()
tess.color("blue")
tess.pensize(3)
tess.penup()
for i, temperature in enumerate(temperatures_list):

    x = i * 20
    y = (temperature - min_temperature) * dy + 350
    tess.goto(x, y)
    tess.pendown()


turtle.done()
