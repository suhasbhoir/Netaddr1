from netaddr import IPNetwork, cidr_merge
import time

while True:

    start = time.time()
    try:
        select_file = input("Please enter the 'Text file' name here: - ")
        total_ip_sub = []
        for line in open(select_file, 'r').readlines():
            total_ip_sub.append(IPNetwork(line.strip()))
        no_ip_sub = (len(total_ip_sub))
        print(f'Total {no_ip_sub} Ip subnets need to be Summarize')
        ip_summarization = cidr_merge(total_ip_sub)
        # file = 'Summarized_subnets.txt'
        after_summarize = len(ip_summarization)
        ex_sum = (f'Total {after_summarize} IP subnets are remained out of {no_ip_sub} IP subnets')
        print(ex_sum)
        output_summary = input("please enter the output file name in '.txt' format: - ")
        for ip_subnets in ip_summarization:
            print(ip_subnets)
            with open(output_summary, 'a') as bkp:
                bkp.writelines(str(ip_subnets))
                bkp.writelines('\n')
                bkp.close()
        print(f'Summarized subnets are capture in text file in same directory')


        end = time.time()
        print(f'Total {no_ip_sub} routes are summarize within {end-start} ')
        print('\nCode written by SUHAS B.')

        print('Please enter "Yes" for another ip subnet text file to summarizing or "No" to quit the Code')
        repl = input("Enter Yes/No: ").lower
        if repl == 'no':
            break
        elif repl == 'yes':
            continue
        else:
            print('Invalid input entered')

    except FileNotFoundError as f:
        print(f'\n"{select_file}" file not found in current repository, Please enter the valid file name in same directory\n')
    finally:
        print("exiting from Code... Thanks for using this code\n")







