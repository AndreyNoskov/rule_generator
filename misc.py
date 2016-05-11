import random
import statistics


def generate_random_mac(vendor_list):
    vendor_id = random.choice(vendor_list)
    mac = [int(vendor_id[0], 16),
           int(vendor_id[1], 16),
           int(vendor_id[2], 16),
           random.randint(0x00, 0x7f),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff)]

    return ':'.join(map(lambda x: "%02x" % x, mac))


def generate_random_local_ip():
    octets_list = []
    if random.random() > 0.5:
        octets_list.append(192)
        octets_list.append(168)
    else:
        octets_list.append(10)
        octets_list.append(0)
    octets_list.append(random.randint(0, 255))
    octets_list.append(random.randint(0, 255))
    ip_str = str(octets_list[0])
    for octet in octets_list[1:len(octets_list)]:
        ip_str += "." + str(octet)
    ip_str += "/32"
    return ip_str


def generate_random_wide_ip():
    octets_list = []
    for octet in range(0, 4):
        octets_list.append(random.randint(0, 255))
    ip_str = str(octets_list[0])
    for octet in octets_list[1:len(octets_list)]:
        ip_str += "." + str(octet)
    ip_str += "/32"
    return ip_str


def about_times(times):
    stat = {}
    total_time = sum(times)
    stat.update({"total time": total_time})
    average = statistics.mean(times)
    stat.update({"average time": average})
    if len(times) > 1:
        st_dev = statistics.stdev(times)
        stat.update({"STDev time": st_dev})
    else:
        stat.update({"STDev time": 0})
    return stat
