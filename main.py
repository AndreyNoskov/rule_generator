import json
from generator import Generator
from sender import Sender
from updater import Updater
import pprint
import time
from misc import about_times

with open('config.json') as config_file:
    config = json.load(config_file)

generator = Generator(config)
sender = Sender(config)
updater = Updater(config)

updater.update_switches()
updater.update_ips()

pp = pprint.PrettyPrinter(indent=4)

success_counter = 0
number_of_rules = 1000
times = []

for i in range(number_of_rules):
    rule = generator.create_rule()
    print("Rule #" + str(i + 1))
    pp.pprint(rule)
    startTime = time.time()
    if sender.send(rule):
        success_counter += 1
    times.append(time.time() - startTime)

print(str(success_counter) + " of " + str(number_of_rules) + " rules was successfully installed")
print(about_times(times))
