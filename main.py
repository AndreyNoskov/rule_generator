import json
from generator import Generator
from sender import Sender
from updater import Updater
import pprint
import time
from misc import about_times
from plotter import plot_time_per_rule

try:
    with open('config.json') as config_file:
        config = json.load(config_file)
except FileNotFoundError:
    print("Can not found config file")
    exit()

generator = Generator(config)
sender = Sender(config)
updater = Updater(config)

updater.update_switches()
updater.update_ips()

pp = pprint.PrettyPrinter(indent=4)

installed_counter = 0
deleted_counter = 0
number_of_rules = 0
from_file = config["rule_generator"]["parameters"]["from_file"]
if from_file:
    log_name = config["rule_generator"]["parameters"]["file_name"]
    try:
        rule_list = generator.create_from_file(log_name)
        number_of_rules = len(rule_list)
    except FileNotFoundError:
        print("Can not find file " + log_name)
        exit()
else:
    number_of_rules = config["rule_generator"]["parameters"]["number_of_rules"]
times = []


time_str = time.strftime("%Y%m%d-%H%M%S")
with open('./rules_log/' + time_str + '.txt', 'w') as log_file:
    for i in range(number_of_rules):
        startTime = time.time()
        rule = rule_list[i] if from_file else generator.create_rule()
        add_ins, add_del = sender.send(rule)
        installed_counter += add_ins
        deleted_counter += add_del
        times.append(time.time() - startTime)
        log_file.write(str(rule) + '\n')
        print("Rule #" + str(i + 1))
        pp.pprint(rule)

print(str(installed_counter) + " of " + str(number_of_rules) + \
      " rules was successfully installed and " + str(deleted_counter) + " was deleted")
print(about_times(times))
plot_time_per_rule(times)

