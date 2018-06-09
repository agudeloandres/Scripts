import urllib2
import json
from urllib2 import urlopen

import re

# Get Public IP

weatherAPI_Key='a936f4f50b688bb2c0918f4dea1f72e2'

def getPublicIP():
        data = str(urlopen('http://checkip.dyndns.com/').read())
        return re.compile(r'Address: (\d+.\d+.\d+.\d+)').search(data).group(1)

IP = str(getPublicIP())

#print 'Your IP is ' + IP

# Get Location
url = 'http://ipinfo.io/' + IP + '/json'
response = urlopen(url)
data = json.load(response)
city = data['city']

# Get Weather
#'http://api.openweathermap.org/data/2.5/weather?q=' + city)
weather_URL='http://api.openweathermap.org/data/2.5/weather?q='+ city+'&APPID='+weatherAPI_Key #+'&units=metric'
response = urllib2.urlopen(weather_URL)
data = json.load(response)

#print  weather_URL
#print data
print "Your City : " + city
print "Current Weather : " + str(data['main']['temp'] - 273) + "C"
