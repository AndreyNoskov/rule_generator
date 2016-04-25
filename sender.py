import requests


class Sender:

    ip_address = None
    port = None

    def __init__(self, config):
        self.config = config
        self.ip_address = config["controller"]["ip"]
        self.port = str(config["controller"]["port"])

    def send(self, rule):
        url = 'http://' + self.ip_address + ":" + self.port + '/wm/firewall/rules/json'
        r = requests.post(url, data=rule)
        print('-------Response:-------')
        print(r.text)
        print(r.json)
        print('-----------------------')


