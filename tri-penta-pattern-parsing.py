


pip install requests python-nmap

import os
import re
import datetime
import socket
import requests
import nmap
import random

# Define patterns and anti-patterns
PATTERNS = {
    'list_comprehension': re.compile(r'\[.* for .* in .*\]'),
}

ANTI_PATTERNS = {
    'global_variable': re.compile(r'global\s+\w+'),
}

PENTA_PATTERNS = {
    'reverse_list_comprehension': re.compile(r'\[.* for .* in .*\]')
}

def get_metadata(subnet):
    """Collect metadata including timestamp, IP address, and subnet devices."""
    timestamp = datetime.datetime.now().isoformat()
    ip_address = socket.gethostbyname(socket.gethostname())

    # Optionally, get public IP address
    try:
        public_ip = requests.get('https://api.ipify.org').text
    except requests.RequestException:
        public_ip = 'Unavailable'

    # Scan the subnet for devices
    nm = nmap.PortScanner()
    nm.scan(hosts=subnet, arguments='-sn')
    devices = [(host, nm[host]['status']['state']) for host in nm.all_hosts()]

    return {
        'timestamp': timestamp,
        'ip_address': ip_address,
        'public_ip': public_ip,
        'devices': devices
    }

def analyze_file(file_path):
    """Analyze a file for patterns, anti-patterns, and penta patterns."""
    with open(file_path, 'r') as file:
        content = file.read()

    results = {
        'patterns': {},
        'anti_patterns': {},
        'penta_patterns': {}
    }

    # Check for patterns
    for pattern_name, pattern_regex in PATTERNS.items():
        matches = pattern_regex.findall(content)
        if matches:
            results['patterns'][pattern_name] = matches

    # Check for anti-patterns
    for anti_pattern_name, anti_pattern_regex in ANTI_PATTERNS.items():
        matches = anti_pattern_regex.findall(content)
        if matches:
            results['anti_patterns'][anti_pattern_name] = matches

    # Check for penta patterns
    for penta_pattern_name, penta_pattern_regex in PENTA_PATTERNS.items():
        matches = penta_pattern_regex.findall(content)
        if matches:
            results['penta_patterns'][penta_pattern_name] = matches

    return results

def reverse_engineer_penta_patterns(content):
    """Reverse engineer penta patterns in the content."""
    # Example: Reverse list comprehensions
    reversed_content = content
    for match in PENTA_PATTERNS['reverse_list_comprehension'].findall(content):
        reversed_content = reversed_content.replace(match, f"reversed({match})")
    return reversed_content

def distort_code(content):
    """Distort code to introduce subtle changes."""
    distorted_content = content
    # Example distortion: Add random comments
    lines = distorted_content.split('\n')
    for i in range(len(lines)):
        if random.random() < 0.1:  # 10% chance to add a comment
            lines[i] += f"  # Random comment {random.randint(1, 1000)}"
    distorted_content = '\n'.join(lines)
    return distorted_content

def analyze_directory(directory_path):
    """Analyze all Python files in a directory for patterns, anti-patterns, and penta patterns."""
    results = {}
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                results[file_path] = analyze_file(file_path)
    return results

def main():
    directory_path = input("Enter the directory path to analyze: ")
    subnet = input("Enter the subnet to scan (e.g., 192.168.1.0/24): ")
    metadata = get_metadata(subnet)
    results = analyze_directory(directory_path)

    print(f"Analysis performed at: {metadata['timestamp']}")
    print(f"Local IP Address: {metadata['ip_address']}")
    print(f"Public IP Address: {metadata['public_ip']}")
    print("Devices in subnet:")
    for device, status in metadata['devices']:
        print(f"  {device}: {status}")
    print()

    for file_path, result in results.items():
        print(f'File: {file_path}')
        if result['patterns']:
            print('  Patterns:')
            for pattern_name, matches in result['patterns'].items():
                print(f'    {pattern_name}: {matches}')
        if result['anti_patterns']:
            print('  Anti-Patterns:')
            for anti_pattern_name, matches in result['anti_patterns'].items():
                print(f'    {anti_pattern_name}: {matches}')
        if result['penta_patterns']:
            print('  Penta Patterns:')
            for penta_pattern_name, matches in result['penta_patterns'].items():
                print(f'    {penta_pattern_name}: {matches}')
                with open(file_path, 'r') as file:
                    content = file.read()
                reversed_content = reverse_engineer_penta_patterns(content)
                distorted_content = distort_code(reversed_content)
                with open(file_path, 'w') as file:
                    file.write(distorted_content)
                print(f'    Reversed and distorted {penta_pattern_name} in {file_path}')
        print()

if __name__ == '__main__':
    main()

python defensive_counter_intel.py
