from __future__ import print_function
import netaddr;

ipranges = [
	['94.127.8.240','94.127.8.240'],
	['151.0.206.160','151.0.206.165'],
	['193.173.12.30','193.173.12.30']
]
#print ipranges;

f = open('cidr_ranges.txt','w')

for range in ipranges:
	f.write('Range: ' + str(range) + ' is CIDR: ' + str(netaddr.iprange_to_cidrs(range[0], range[1])) + '\n' )