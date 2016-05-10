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
                try:
                    resp_json = json.loads(r.text)
                    if "status" in resp_json and resp_json["status"] == "Rule added":
                        if "deleted" in resp_json:
                            return 1, resp_json["deleted"]
                        else:
                            return 1, 0
                    else:
                        return 0, 0
                except ValueError:  # For Python 3.4. Replace for JSONDecodeError for 3.5+
                    print("Can not parse response from firewall to JSON format")
                    return 0, 0
            else:
                return 0, 0
        except requests.exceptions.RequestException:
            print("Connection error while sending rule")
            return 0, 0


