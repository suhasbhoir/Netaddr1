from netaddr import IPAddress, IPNetwork, cidr_merge
import time

start = time.time()

total_ip_sub = []
for line in open('route.txt', 'r').readlines():
    total_ip_sub.append(IPNetwork(line.strip()))
# print(total_ip_sub)
no_ip_sub = (len(total_ip_sub))
print(f'Total {no_ip_sub} Ip subnets need to be Summarize')
ip_summarization = cidr_merge(total_ip_sub)
file = 'Summarized_subnets.txt'
after_summarize = len(ip_summarization)
ex_sum = (f'Total {after_summarize} IP subnets are remained out of {no_ip_sub} IP subnets')
print(ex_sum)
for ip_subnets in ip_summarization:
    print(ip_subnets)
    with open('Summarized_subnets.txt', 'a') as bkp:
        bkp.writelines(str(ip_subnets))
        bkp.writelines('\n')
        bkp.close()
print(f'Summarized subnets are capture in text file in same directory')

end = time.time()
print(f'Total {no_ip_sub} routes are summarize within {end-start} ')
print('\nScript written by SUHAS B.')


