import requests
import json
import pprint


class Updater:

    controller_ip = ''
    controller_port = ''

    def __init__(self, config):
        self.config = config
        self.controller_ip = self.config["controller"]["ip"]
        self.controller_port_rest = self.config["controller"]["port_rest"]
        self.controller_port_pfw = self.config["controller"]["port_pfw"]
        self.pp = pprint.PrettyPrinter(indent=4)

    def update_switches(self):
        try:
            url = 'http://' + self.controller_ip + ":" + self.controller_port_rest + '/wm/core/controller/switches/json'
            r = requests.get(url)
            if r.status_code == 200:
                resp_json = json.loads(r.text)
                for entry in resp_json:
                    self.config["controller"]["switch_id"].append(entry["switchDPID"])
                print("List of switches was successfully updated!")
            else:
                print("List of switches was not updated!")
        except requests.exceptions.RequestException:
            print("Connection error while update switches ID list")

    def update_ips(self):
        try:
            url = 'http://' + self.controller_ip + ":" + self.controller_port_rest + '/wm/device/'
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
        except requests.exceptions.RequestException:
            print("Connection error while update IP list")

