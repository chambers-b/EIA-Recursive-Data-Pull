import os
import requests
import json


def oodles_of_loops(complex_object, path_pass):
    try:
        for route in complex_object['routes']:
            path = path_pass + route['id'] + '/'
            response = requests.request("GET", url + path + api, headers=headers)
            next_route = response.json()['response']
            oodles_of_loops(next_route, path)
    except:
        print('---End of Route')
        print(url + path_pass + api)
        f.write(url + path_pass + api + "\n") 
        print(complex_object['id'])
    return

f = open("URL_List.txt", "a")

sub = {}
url = 'https://api.eia.gov/v2/'
api = '?api_key=excelmacro'
payload = json.dumps({})
headers = {
#  'Content-Type': 'application/x-www-form-urlencoded facets[stateid][]=CO&facets[sectorid][]=RES&frequency=monthly' 
}
response = requests.request("GET", url + api, headers=headers)
top = response.json()['response']
print(top)
oodles_of_loops(top, '')
f.close()

