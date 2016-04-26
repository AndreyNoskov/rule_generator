import requests
import json
import pprint


class Updater:

    controller_ip = ''
    controller_port = ''

    def __init__(self, config):
        self.config = config
        self.controller_ip = self.config["controller"]["ip"]
        self.controller_port = self.config["controller"]["port"]
        self.pp = pprint.PrettyPrinter(indent=4)

    def update_switches(self):
        url = 'http://' + self.controller_ip + ":" + self.controller_port + '/wm/core/controller/switches/json'
        r = requests.get(url)
        if r.status_code == 200:
            resp_json = json.loads(r.text)
            for entry in resp_json:
                self.config["controller"]["switch_id"].append(entry["switchDPID"])
            # self.pp.pprint(self.config["controller"]["switch_id"])
            print("List of switches was successfully updated!")
        else:
            print("List of switches was not updated!")

    def update_ips(self):
        url = 'http://' + self.controller_ip + ":" + self.controller_port + '/wm/device/'
        r = requests.get(url)
        if r.status_code == 200:
            resp_json = json.loads(r.text)
            for entry in resp_json:
                list_ipv4 = entry["ipv4"]
                if len(list_ipv4) != 0:
                    self.config["controller"]["local_ip"].append(list_ipv4[0])
            # self.pp.pprint(self.config["controller"]["local_ip"])
            print("List of local ips was successfully updated!")
        else:
            print("List of local ips was not updated!")
