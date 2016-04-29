import json
from generator import Generator
from sender import Sender
from updater import Updater
import pprint


with open('config.json') as config_file:
    config = json.load(config_file)

generator = Generator(config)
sender = Sender(config)
updater = Updater(config)

updater.update_switches()
updater.update_ips()

pp = pprint.PrettyPrinter(indent=4)

# pp.pprint(config)

for i in range(1, 10):
    rule = generator.create_rule()
    print("Rule #" + str(i))
    pp.pprint(rule)
    sender.send(rule)
