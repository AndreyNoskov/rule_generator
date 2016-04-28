import requests
import json

class Sender:

    ip_address = None
    port = None

    def __init__(self, config):
        self.config = config
        self.ip_address = config["controller"]["ip"]
        self.port_pfw = str(config["controller"]["port_pfw"])

    def send(self, rule):
        try:
            url = 'http://' + self.ip_address + ":" + self.port_pfw + '/wm/firewall/rules/json'
            r = requests.post(url, data=json.dumps(rule))
            print('-------Response:-------')
            print(r.text)
            print('-----------------------\n')
        except requests.exceptions.RequestException:
            print("Connection error while sending rule")


