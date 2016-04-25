import random


def generate_random_mac(vendor_list):
    vendor_id = random.choice(vendor_list)
    mac = [int(vendor_id[0], 16),
           int(vendor_id[1], 16),
           int(vendor_id[2], 16),
           random.randint(0x00, 0x7f),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff)]

    return ':'.join(map(lambda x: "%02x" % x, mac))
