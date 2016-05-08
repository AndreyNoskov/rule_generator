import json
from generator import Generator
from sender import Sender
from updater import Updater
import pprint
import time
from misc import about_times
from plotter import plot_time_per_rule

with open('config.json') as config_file:
    config = json.load(config_file)

generator = Generator(config)
sender = Sender(config)
updater = Updater(config)

updater.update_switches()
updater.update_ips()

pp = pprint.PrettyPrinter(indent=4)

installed_counter = 0
deleted_counter = 0
number_of_rules = 2000
times = []

for i in range(number_of_rules):
    startTime = time.time()
    rule = generator.create_rule()
    add_ins, add_del = sender.send(rule)
    installed_counter += add_ins
    deleted_counter += add_del
    times.append(time.time() - startTime)

    print("Rule #" + str(i + 1))
    pp.pprint(rule)

print(str(installed_counter) + " of " + str(number_of_rules) + \
	" rules was successfully installed and " + str(deleted_counter) + " was deleted")
print(about_times(times))
plot_time_per_rule(times)

