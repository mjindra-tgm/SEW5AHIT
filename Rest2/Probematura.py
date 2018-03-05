import requests
import json

if __name__ == '__main__':
    headers=headers = {"content-type": "application/json"}
    params = {"origin":"wien", "destination":"graz", "language":"de","sensor":"false"}
    res = requests.get("http://maps.googleapis.com/maps/api/directions/json",params, headers=headers)
    print(res.content)

