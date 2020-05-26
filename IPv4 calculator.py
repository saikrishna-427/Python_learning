import ipaddress


class IP4Addres:
    def __init__(self, ip_lst, s_mask):
        self.ip_lst = ip_lst
        self.s_mask = s_mask

    def getMask(self):
        octant = 7
        octant_mask = 0
        mask_lst = list()
        network_bits = 32 - self.s_mask
        # mask = ipaddress.IPv4Address._ip_int_from_prefix(self.s_mask)
        # smask = ipaddress.IPv4Network(mask).netmask
        for i in range(0, self.s_mask):
            octant_mask += 2 ** octant
            octant = octant - 1
            if octant < 0 and i == self.s_mask - 1:
                mask_lst.append(octant_mask)
            elif i == self.s_mask - 1:
                mask_lst.append(octant_mask)
            else:
                if octant < 0:
                    mask_lst.append(octant_mask)
                    octant_mask = 0
                    octant = 7
        for oct1 in range(4):
            if len(mask_lst) < 4:
                mask_lst.append(0)
        return mask_lst

    def getNetwork(self):
        ip_address = self.ip_lst
        subnet_mask = IP4Addres.getMask(self)
        network_address = list()
        for i in range(len(ip_address)):
            network_address.append(ip_address[i] & subnet_mask[i])
        return network_address

    def getFirstIP(self):
        first_ip =[]
        for i in range(4):
            if i == 3:
                first_ip.append(self.getNetwork()[i]+1)
            else:
                first_ip.append(self.getNetwork()[i])
        return first_ip



    def getLastIP(self):
        last_ip = []
        for i in range(4):
            if self.getMask()[i] == 255:
                last_ip.append(self.getNetwork()[i])
            else:
                last_ip.append(self.getNetwork()[i] + self.getMask()[i] - 2)
        return last_ip

    def getBrodcast_IP(self):
        broadcast_ip = []
        for i in range(4):
            if self.getMask()[i] == 255:
                broadcast_ip.append(self.getNetwork()[i])
            else:
                broadcast_ip.append(self.getNetwork()[i] + self.getMask()[i] - 1)
        return broadcast_ip



ipv4 = IP4Addres([11, 254, 44, 4], 25)
print(ipv4.__dict__)

subnetmask = ipv4.getMask()
print(subnetmask)
network = ipv4.getNetwork()
print(network)
first_ip = ipv4.getFirstIP()
print('first ip of given IP is :'str(first_ip))
last_ip = ipv4.getLastIP()
print('Last ip of given IP is: '+ str(last_ip))
broadcast_ip = ipv4.getBrodcast_IP()
print('broadcast IP is:' + str(broadcast_ip))