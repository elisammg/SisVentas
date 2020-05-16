import urllib.request as ur
import json


url = "http://192.168.1.19:8080/rtproductos"
response = ur.urlopen(url)
data = json.loads(response.read())

print (data)






