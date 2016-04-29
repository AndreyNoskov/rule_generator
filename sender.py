import requests
import json


class Sender:

    def __init__(self, config):
        self.config = config
        self.ip_address = config["controller"]["ip"]
        self.port_pfw = str(config["controller"]["port_pfw"])

    def send(self, rule):
        try:
            url = 'http://' + self.ip_address + ":" + self.port_pfw + '/wm/firewall/rules/json'
            # print(url)
            r = requests.post(url, data=json.dumps(rule))
            print('-------Response:-------')
            # print(r.status_code)
            print(r.text)
            print('-----------------------\n')
            if r.status_code == 200:
                resp_json = json.loads(r.text)
                if resp_json["status"] == "Rule added":
                    return True
            else:
                return False
        except requests.exceptions.RequestException:
            print("Connection error while sending rule")
            return False


