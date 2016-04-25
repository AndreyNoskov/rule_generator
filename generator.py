import random
from misc import *


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
        return rule

    def create_switch_id(self, rule):
        """ Create switch_id field of firewall rule if generated number greater
        then config probability or pass otherwise. Generated switch_id get from
        list of available values """
        prob = self.config["rule_generator"]["switch_id"]["probability"]
        if random.random() > prob:
            list_of_switches = self.config["rule_generator"]["switch_id"]["list"]
            if len(list_of_switches) == 0:
                pass
            else:
                rule.update({"switchid": random.choice(list_of_switches)})
        else:
            pass

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
        prob = self.config["rule_generator"]["src_ip"]["probability"]
        ip_address = []
        if random.random() > prob:
            octets = self.config["rule_generator"]["src_ip"]["octets"]
            if random.random() > self.config["rule_generator"]["src_ip"]["is_local"]:
                for octet in ["A", "B", "C", "D"]:
                    if octets[octet] == "any":
                        ip_address.append(random.randint(0, 256))
                    else:
                        ip_address.append(int(octets[octet]))
            else:
                if random.random() > 0.5:
                    ip_address.append(192)
                    ip_address.append(168)
                else:
                    ip_address.append(10)
                    ip_address.append(0)
                for octet in ["C", "D"]:
                    if octets[octet] == "any":
                        ip_address.append(random.randint(0, 256))
                    else:
                        ip_address.append(int(octets[octet]))
            ip_str = str(ip_address[0])
            for octet in range(1, 4):
                ip_str += "." + str(ip_address[octet])
            rule.update({"src-ip": ip_str})
        else:
            pass

    def create_dst_ip(self, rule):
        """ Create dst_ip field of firewall rule if generated number greater
            then config probability or pass otherwise. """
        prob = self.config["rule_generator"]["dst_ip"]["probability"]
        ip_address = []
        if random.random() > prob:
            octets = self.config["rule_generator"]["dst_ip"]["octets"]
            if random.random() > self.config["rule_generator"]["dst_ip"]["is_local"]:
                for octet in ["A", "B", "C", "D"]:
                    if octets[octet] == "any":
                        ip_address.append(random.randint(0, 256))
                    else:
                        ip_address.append(int(octets[octet]))
            else:
                if random.random() > 0.5:
                    ip_address.append(192)
                    ip_address.append(168)
                else:
                    ip_address.append(10)
                    ip_address.append(0)
                for octet in ["C", "D"]:
                    if octets[octet] == "any":
                        ip_address.append(random.randint(0, 256))
                    else:
                        ip_address.append(int(octets[octet]))
            ip_str = str(ip_address[0])
            for octet in range(1, 4):
                ip_str += "." + str(ip_address[octet])
            rule.update({"dst-ip": ip_str})
        else:
            pass
