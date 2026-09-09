import os
import sys
import time 
import csv 
import json 
import subprocess

from datetime import datetime
# sniff wifi packets capture 
from scapy.all import sniff
# scapy 802.11 wifi layer
from scapy.layers.dot11 import *
from tabulate import tabulate 

DATA_DIR = 'data'
LOGS_DIR = 'logs'
REPORTS_DIR = 'reports'

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(LOGS_DIR, exist_ok=True)
os.makedirs(REPORTS_DIR, exist_ok=True)

DEFAULT_INTERFACE = None
SCAN_TIMEOUT = 10
LOG_FILE = os.path.join(LOGS_DIR, 'wifi_tool.log')
RESULTS_FILE = os.path.join(DATA_DIR, 'networks.csv')

TOOL_NAME = 'wifi security recon tool'
TOOL_VERSION = '1.0'
AUTHOR = 'liyanda'
DESCRIPTION = 'Find nearby wifi networks and analyse security details'

def show_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
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
    
