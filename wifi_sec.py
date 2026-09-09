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
from scapy.layers.dot11 import DOt11
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


