""" The pprint module provides a capability to "pretty-print"
arbitrary Python data structures in a well-formatted and more readable
way"""

import  requests

def geocode(addr):
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    resp = requests.get(url,params={'address':addr})
    return resp.json()

data = geocode('India gate')
print(data)













