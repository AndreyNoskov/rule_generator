import random
from misc import *
import json


class Generator:

    def __init__(self, config):
        # constructor
        self.config = config
        random.seed()

    def create_rule(self):
        """ Create rule based on config file """
        rule = {}
        self.create_switch_id(rule)
        self.create_src_inport(rule)
        self.create_src_mac(rule)
        self.create_dst_mac(rule)
        self.create_dst_ip(rule)
        self.create_src_ip(rule)
        self.create_action(rule)
        self.create_priority(rule)
        return rule

    def create_from_file(self, log_path):
        with open(log_path, "r") as log:
            rules = log.read().splitlines()
            rules_out = []
            for rule in rules:
                # rule = json.JSONDecoder.decode(rule)
                # json_text = json.loads(rule, encoding="utf-8")
                rules_out.append(rule)
        return rules_out

    def create_switch_id(self, rule):
        """ Create switch_id field of firewall rule if generated number greater
        then config probability or pass otherwise. Generated switch_id get from
        list of available values """
        prob = self.config["rule_generator"]["switch_id"]["probability"]
        if random.random() > prob:
            if len(self.config["controller"]["switch_id"]) == 0:
                list_of_switches = self.config["rule_generator"]["switch_id"]["def_list"]
            else:
                list_of_switches = self.config["controller"]["switch_id"]
            rule.update({"switchid": random.choice(list_of_switches)})

    def create_src_inport(self, rule):
        """ Create switch_id field of firewall rule if generated number greater
        then config probability or pass otherwise """
        prob = self.config["rule_generator"]["src_inport"]["probability"]
        if random.random() > prob:
            min_value = self.config["rule_generator"]["src_inport"]["min_value"]
            max_value = self.config["rule_generator"]["src_inport"]["max_value"]
            rule.update({"src-inport": random.randint(min_value, max_value)})
        else:
            pass

    def create_src_mac(self, rule):
        """ Create src_mac field of firewall rule if generated number greater
            then config probability or pass otherwise. First three parts get
            from lest_vendor_id randomly. """
        prob = self.config["rule_generator"]["src_mac"]["probability"]
        if random.random() > prob:
            vendor_list = self.config["rule_generator"]["src_mac"]["list_vendor_id"]
            rule.update({"src-mac": generate_random_mac(vendor_list)})
        else:
            pass

    def create_dst_mac(self, rule):
        """ Create dst_mac field of firewall rule if generated number greater
            then config probability or pass otherwise. First three parts get
            from lest_vendor_id randomly. """
        prob = self.config["rule_generator"]["dst_mac"]["probability"]
        if random.random() > prob:
            vendor_list = self.config["rule_generator"]["dst_mac"]["list_vendor_id"]
            rule.update({"dst-mac": generate_random_mac(vendor_list)})
        else:
            pass

    def create_src_ip(self, rule):
        """ Create src_ip field of firewall rule if generated number greater
            then config probability or pass otherwise. """
        if random.random() > self.config["rule_generator"]["src_ip"]["probability"]:
            if random.random() > self.config["rule_generator"]["src_ip"]["is_local"]:
                if len(self.config["controller"]["local_ip"]) != 0:
                    ip = random.choice(self.config["controller"]["local_ip"])
                else:
                    ip = generate_random_local_ip()
            else:
                ip = generate_random_wide_ip()
            rule.update({"src-ip": ip})

    def create_dst_ip(self, rule):
        """ Create dst_ip field of firewall rule if generated number greater
            then config probability or pass otherwise. """
        if random.random() > self.config["rule_generator"]["dst_ip"]["probability"]:
            if random.random() > self.config["rule_generator"]["dst_ip"]["is_local"]:
                if len(self.config["controller"]["local_ip"]) != 0:
                    ip = random.choice(self.config["controller"]["local_ip"])
                else:
                    ip = generate_random_local_ip()
            else:
                ip = generate_random_wide_ip()
            rule.update({"dst-ip": ip})

    def create_action(self, rule):
        """ Create action "ALLOW" field of firewall rule if generated number greater
            then config probability or "DENY" otherwise. """
        prob = self.config["rule_generator"]["action"]["probability"]
        value_dict = self.config["rule_generator"]["action"]["values"]
        if random.random() > prob:
            rule.update({"action": value_dict["ALLOW"]})
        else:
            rule.update({"action": value_dict["DENY"]})

    def create_priority(self, rule):
        """ Create priority field of firewall rule if generated number greater
            then config probability or pass otherwise. Values are picked from
            range[min_value, max_value] """
        prob = self.config["rule_generator"]["priority"]["probability"]
        if random.random() > prob:
            range_values = self.config["rule_generator"]["priority"]["values"]
            value = random.randint(range_values["min_value"], range_values["max_value"])
            rule.update({"priority": value})

    def create_nw_proto(self, rule):
        """ Create nw-proto field of firewall rule if generated number greater
            then config probability or pass otherwise. """
        nw_proto = self.config["rule_generator"]["nw_proto"]
        if random.random() > nw_proto["probability"]:
            rnd_val = random.random()
            if 0 <= rnd_val < nw_proto["values"]["ICMP"]:
                rule.update({"nw-proto": "ICMP"})
            if nw_proto["values"]["ICMP"] <= rnd_val < nw_proto["values"]["TCP"]:
                rule.update({"nw-proto": "TCP"})
            if nw_proto["values"]["TCP"] <= rnd_val <= nw_proto["values"]["UDP"]:
                rule.update({"nw-proto": "UDP"})
