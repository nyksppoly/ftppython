# Ref: https://www.studytonight.com/network-programming-in-python/integrating-port-scanner-with-nmap
# Ref: https://pypi.org/project/python-nmap/
# Name of script: nmap-scan-sample.py
#  """
#  Purpose:
#    Script to print results of port scan
#
#  Run: 
#    Nil
#
#  Args:
#    Nil
#
#  Output:
#    Prints items such as host, protocol, port and state after a port scan
#  """  

# main starts here
import nmap
from prettytable import PrettyTable

# initialize the port scanner
nmScan = nmap.PortScanner()
print(f'Type of nmScan : {type(nmScan)}')

def scannetwork():
  # scan multiple hosts/specify options
  IP = 'localhost scanme.nmap.org'                                     # IPs separated by a space
  print(f'Target IP      : {IP}')

  options = '--top-ports 10 -sT -sU -T5 -O -sC -sV --version-intensity 1'                        # scanning top 10 most used TCP and UDP ports
  results = nmScan.scan(hosts=IP, arguments=options)

  # print items in dict. Nmap has provided several methods.
  print(f'Command Line Used: {nmScan.command_line()}')
  print(f'Scaninfo         : {nmScan.scaninfo()}')

  # You have to explore other methods to do your assignment, especailly those below
  print(f' All hosts    : {nmScan.all_hosts()}')
  print(f' All protocols: {nmScan["127.0.0.1"].all_protocols()}')
  print(f' All ports tcp: {nmScan["127.0.0.1"]["tcp"].keys()}')   # May have run-time error is no tcp port is open
  print(f' All ports udp: {nmScan["127.0.0.1"]["udp"].keys()}')   # May have run-time error is no udp port is open
  print('**********')

  # starting table to be printed
  printed = PrettyTable()
  hostnum = []
  hostname = []
  protocolname = []
  portid = []
  portstate = []
  productinfo = []
  extrainfo = []
  reason = []
  cpeinfo = []
  # Review the structure of the dict [initial scan] - scan-tcp-udp-dict.pdf
  for host in nmScan.all_hosts():
    for proto in nmScan[host].all_protocols():
      # print(nmScan[host][proto].keys())
      for port in nmScan[host][proto].keys():
        hostnum += {host}
        hostname += {nmScan[host].hostname()}
        protocolname += {proto}
        portid += {port}
        portstate += {nmScan[host][proto][port]["state"]}
        productinfo += {nmScan[host][proto][port]['product']}
        extrainfo += {nmScan[host][proto][port]['extrainfo']}
        reason += {nmScan[host][proto][port]['reason']}
        cpeinfo += {nmScan[host][proto][port]['cpe']}
  printed.add_column("Host", hostnum)
  printed.add_column("Hostname", hostname)
  printed.add_column("Protocol", protocolname)
  printed.add_column("Port", portid)
  printed.add_column("State", portstate)
  printed.add_column("Product", productinfo)
  printed.add_column("Extrainfo", extrainfo)
  printed.add_column("Reason", reason)
  printed.add_column("CPE", cpeinfo)
  print(printed)
  

scannetwork()