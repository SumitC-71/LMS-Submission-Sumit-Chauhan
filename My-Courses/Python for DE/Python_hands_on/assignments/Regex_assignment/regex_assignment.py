from collections import defaultdict
import datetime
import json
import re

filename = 'data_log.txt'

'''
1. Extract All IP Addresses
Write a regex to extract all the IP addresses from the log. Print the unique IP addresses in sorted order.
'''
def extract_ips():
    with open(filename,'r') as r:
        unique_ips = set()
        for line in r:
            # Extracting all ips from single line
            ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
            ips = re.findall(ip_pattern,line)
            for ip in ips:
                unique_ips.add(ip)
        unique_ips = list(unique_ips)
        unique_ips.sort()
        
        print('All unique ips')
        for ip in unique_ips:
            print(ip)
        return unique_ips


'''
2. Extract User Actions
    For all log lines containing "INFO," extract:
        The username (e.g., john_doe).
        The action they performed (e.g., 'UPDATE' or 'created a new record').
    Store the results in a dictionary where the key is the username and the value is a unique list of their actions.
'''

def extract_user_actions():
    userActions = defaultdict(set)

    with open(filename,'r') as r:
        for line in r:
            # check for INFO logs only
            if re.search('INFO',line):
                pattern = re.findall(r'User [\w]+ .*',line)
                if len(pattern) == 0: 
                    continue
                pattern = pattern[0]
                pattern = pattern.split(' ')
                
                if len(pattern)<3 or pattern[0] != 'User':
                    continue
                user = pattern[1]
                action = " ".join(pattern[2:])
                userActions[user].add(action)
    print('All users with their actions as set')
    for user,action in userActions.items():
        print(f'User: {user} -> {action}')
    return userActions

# Alternatively we can use pattern like this: r'User (\w+) (.*)' -> this will return [('user_name','action')]

'''
3. Validate and Extract Email Addresses
    Search for valid email addresses in the log file. Ensure the email address adheres to standard rules (e.g., contains @, valid domain, no special characters in the username).
    Output the extracted email addresses.
'''

def validate_and_extract_email():
    emails = set()
    with open(filename,'r') as r:
        for line in r:
            # extracting emails from single line
            valid_emails = re.findall(r'[\w\.-]{2,20}@[a-zA-Z]{2,20}\.[a-zA-Z]{2,3}',line)
            for email in valid_emails:
                emails.add(email)
    print('All Extracted email')
    for email in emails:
        print(email)
    return emails

'''
4. Extract Phone Numbers
    Find and extract all phone numbers in the log. Ensure the phone numbers:
        Follow the format XXX-XXX-XXXX.
        Contain exactly 10 digits.
    Return the extracted numbers in a set
'''

def extract_phone_numbers():
    phone_numbers = set()
    with open(filename,'r') as r:
        for line in r:
            # extracting phone numbers from single line
            numbers = re.findall(r'\d{3}-\d{3}-\d{4}',line)
            for number in numbers:
                phone_numbers.add(number)
    
    # printing all extracted numbers
    print('All Extracted phone numbers')
    for number in phone_numbers:
        print(number)
    return phone_numbers

'''
5. Extract All URLs
    Search for and extract all URLs from the log. Ensure that:
        The URL starts with http:// or https://.
        It includes a valid domain name.
    Return the extracted URLs in a set.
'''


def extract_all_urls():
    all_urls = set()
    with open(filename,'r') as r:
        for line in r:
            # extracting urls from single line
            urls = re.findall(r'(?:http://|https://)[^\s]+\.[^\s]+',line)
            for url in urls:
                all_urls.add(url)

    print('All Extracted emails')
    for url in all_urls:
        print(url)
    return all_urls

'''
6. Classify Log Levels
    Using regex, classify each log entry by its severity level (INFO, WARNING, ERROR, or CRITICAL). 
    Count the number of entries in each category and display the results in a dictionary.
'''

def classify_log_levels():
    logDict = {}
    with open(filename,'r') as r:
        for line in r:
            log_level = re.findall(r'(INFO|WARNING|ERROR|CRITICAL)',line) 

            # a valid log must contain single log level in one line
            if len(log_level) != 1:
                continue
            log_level = log_level[0]

            # storing freq of log_level
            logDict[log_level] = logDict.get(log_level,0) + 1

    print('Log levels, frequency')
    for log_level, freq in logDict.items():
        print(log_level,freq)

    return logDict


'''
7. Extract Timestamps
    Extract all the timestamps (e.g., [2025-01-07 14:32:10]) from the log. 
    Store the timestamps in a list and display them in ascending order.

'''

def extract_timestamps():
    all_timestamps = []
    with open(filename,'r') as r:
        for line in r:
            # extracting timestamp
            timestamps = re.findall(r'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}',line)
            for ts in timestamps:

                # converting ts timestamp string into datetime object
                tms = datetime.datetime.strptime(ts,'%Y-%m-%d %H:%M:%S')
                all_timestamps.append(tms)

    # sorting in ascending order
    all_timestamps.sort()
    print('All timestamps')
    for ts in all_timestamps:
        print(ts)
    return all_timestamps

'''
8. Mask Sensitive Information
    Create a new version of the log where:
        IP addresses are masked as ***.***.***.***.
        Phone numbers are masked as XXX-XXX-XXXX.
        Email addresses are masked as hidden@example.com.
    Save the modified log to a new file named masked_data_log.txt.
'''

def mask_sensitive_info():
    new_file = 'masked_data_log.txt'
    with open(filename,'r') as r:
        with open(new_file,'w') as wf:
            for line in r:
                # patterns
                ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
                phone_pattern = r'\d{3}-\d{3}-\d{4}'
                email_pattern = r'[\w\.-]{2,20}@[a-zA-Z]{2,20}\.[a-zA-Z]{2,3}'
                
                # masking ips
                line = re.sub(ip_pattern,'***.***.***.***',line)
                # masking phone
                line = re.sub(phone_pattern,'XXX-XXX-XXXX',line)
                # replacing email
                line = re.sub(email_pattern,'hidden@example.com',line)

                # writing to new masked log file
                wf.write(line)

                print(f'masked date loaded to masked_data_log.txt file')

'''
9. Validate Error Codes
    Identify and validate error codes from the log. Error codes should:
    Start with DB_ERR_ followed by a 4-digit number.
    Print all unique valid error codes in a list.
'''

def validate_error_codes():
    all_error_codes = []
    with open(filename,'r') as r:
        for line in r:
            # extracting db errors in form of list
            error_codes = re.findall(r'DB_ERR_\d{4}',line)
            for code in error_codes:
                all_error_codes.append(code)

    # printing all unique error codes
    print('All error codes: ')
    for code in set(all_error_codes):
        print(code)
    return all_error_codes


'''
10. Parse Log into Structured Format
    Using regex, parse the log entries into a structured format (dictionary or JSON) with the following keys:
        timestamp: The timestamp of the log entry.
        level: The log level (INFO, WARNING, ERROR, CRITICAL).
        message: The rest of the log message.
    Write the parsed data to a file named parsed_log.json.
'''

def log_parser():
    new_file='parsed_log.json'
    parsed_logs = []
    with open(filename,'r') as r:
        for line in r:
            # patterns
            timestamp_pattern = r'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}'
            level_pattern= r'(INFO|WARNING|ERROR|CRITICAL)'
            
            # extracting keys in form of list 
            # checking if log line contains valid format
            timestamp = re.findall(timestamp_pattern,line)
            if len(timestamp) != 1:
                continue
            level = re.findall(level_pattern,line)
            if len(level) != 1:
                continue
            message = re.findall(r'\[\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\]\s(?:INFO|WARNING|ERROR|CRITICAL):\s(.*)',line)
            if len(message) != 1:
                continue
            
            # log dictionary for single log
            logDict = {
                'timestamp': timestamp[0],
                'level': level[0],
                'message': message[0]
            }
            
            parsed_logs.append(logDict)

    # writing logs to parsed_log.json
    with open(new_file,'w') as wf:
        json.dump(parsed_logs,wf,indent=2)
        print(f'All parsed logs added to {new_file}')

extract_phone_numbers()
