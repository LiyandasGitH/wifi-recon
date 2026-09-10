import os
import sys
import time 
import csv 
import json 
import subprocess

from datetime import datetime 
from scapy.all import sniff # sniff wifi packets capture 
from scapy.layers.dot11 import * # scapy 802.11 wifi layer
from tabulate import tabulate  # to make it pretty 

# project folders
DATA_DIR = 'data'
LOGS_DIR = 'logs'
REPORTS_DIR = 'reports'

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(LOGS_DIR, exist_ok=True)
os.makedirs(REPORTS_DIR, exist_ok=True)

# configuration
DEFAULT_INTERFACE = None # use monitor mode interface
SCAN_TIMEOUT = 10 # seconds to scan networks
LOG_FILE = os.path.join(LOGS_DIR, 'wifi_tool.log')
RESULTS_FILE = os.path.join(DATA_DIR, 'networks.csv')

# tool information
TOOL_NAME = 'wifi security recon tool'
TOOL_VERSION = '1.0'
AUTHOR = 'liyanda'
DESCRIPTION = 'Find nearby wifi networks and analyse security details'

# main menu 
def show_menu():
    subprocess.run(
        'cls' if os.name == 'nt' else 'clear',
        shell=True
    )
    print('=' * 70)
    
    print(f"{TOOL_NAME}     v{TOOL_VERSION}")
    
    print("1. List Wireless Interfaces")
    print("2. Scan Wifi Networks")
    print("3. Analyse Selected Network")
    print("4. Export Results (CSV)")
    print("5. View Saved Results")
    print("6. Exit")
    
    print("-" * 70)

# func : get wifi interfaces
def get_wifi_interface():
    interfaces = []
    for iface in os.listdir('/sys/class/net'):
        if iface != 'lo':
            interfaces.append(iface)
        return interfaces

# func : scan wifi networks
def scan_wifi(interface, timeout = 5):
    networks = []
    print(f'[*] Scanning on {interface}...PLease wait {timeout}s')
    os.system(f'iwlist {interface} scan | tee scan_output.txt') # perform scan & save output 
    time.sleep(timeout)
    with open ('scan_output.txt', 'r', errors='ignore') as f:
        data = f.read().split('Cell') # split each cell/network block
        for cell in data:
            if 'ESSID:' in cell:
                network = parse_network_info(cell) # parse details from each block
                if network:
                    networks.append(network)
    return networks

# func : parse network information
def parse_network_info(cell):   # extract useful info from scan block
    network = {}
    network['BSSID'] = re.search(r'Address:\s*([0-9A-Fa-f:]{17})', cell)
    

