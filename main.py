import json
from generator import Generator
from sender import Sender
import pprint

from misc import *

with open('config.json') as config_file:
    config = json.load(config_file)

generator = Generator(config)
sender = Sender(config)

pp = pprint.PrettyPrinter(indent=4)

for i in range(1, 2):
    rule = generator.create_rule()
    print("Rule #" + str(i))
    pp.pprint(rule)
    #sender.send(rule)

