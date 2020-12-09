from netaddr import IPNetwork, cidr_merge
import time

while True:

    start = time.time()
    try:
        raw_file = input("Please enter the 'Text file' name which contents IPv4 subnets: - ")
        capture_raw = []
        for line in open(raw_file, 'r').readlines():
            capture_raw.append(IPNetwork(line.strip()))
        no_ip_sub = (len(capture_raw))
        print(f'Total {no_ip_sub} Ip subnets need to be Summarize')
        summarize_cidr = cidr_merge(capture_raw)
        # file = 'Summarized_subnets.txt'
        total_summarize_sub = len(summarize_cidr)
        summarize_result = (f' Total {total_summarize_sub} IP subnets are summarize, from {no_ip_sub} IP subnets')
        print(summarize_result)
        output_file = input("please enter the output file name in '.txt' format: - ")
        for ip_subnets in summarize_cidr:
            print(ip_subnets)
            with open(output_file, 'a') as bkp:
                bkp.writelines(str(ip_subnets))
                bkp.writelines('\n')
                bkp.close()
        print(f'Summarized subnets are capture in a text file in the same directory.')


        end = time.time()
        print(f'Total {no_ip_sub} routes are summarize within {end-start} ')
        print('\nCode written by SUHAS B.')

        print('Please enter "Yes" for another ip subnet text file to summarizing or "No" to quit the Code')
        repl = str(input("Enter 'Y' for yes or 'N' for NO: ")).lower()
        if repl == 'y':
            continue
        elif repl == 'n':
            break
        else:
            print('Invalid input detected')

    except FileNotFoundError as f:
        print(f'\n"{raw_file}" file not found in the current directory, Please enter the valid file name in the same directory\n')








