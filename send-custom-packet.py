from scapy.all import send, IP, TCP, ICMP, UDP   
import re
# srp and sr1 is for layer 2, send for layer 3

def send_packet(src_addr:str , src_port:int , dest_addr:str, 
                 dest_port:int, pkt_type:str, pkt_data:str)  -> bool:
  """Create and send a packet based on the provided parameters

  Args:
      src_addr(str) : Source IP address
      src_port(int) : Source Port
      dest_addr(str): Destination IP address
      dest_port(int): Destination Port
      pkt_type(str) : Type of packet (T)TCP, (U)UDP, (I)ICMP echo request. Note it is case sensitive
      pkt_data(str) : Data in the packet
  Returns:
      bool: True if send successfull, False otherwise
  """    

  if pkt_type == "T":
    pkt = IP(dst=dest_addr,src=src_addr)/TCP(dport=dest_port,sport=src_port)/pkt_data
  elif  pkt_type == "U":
    pkt = IP(dst=dest_addr,src=src_addr)/UDP(dport=dest_port,sport=src_port)/pkt_data
  else:
    pkt = IP(dst=dest_addr,src=src_addr)/ICMP()/pkt_data
  try:
    send(pkt ,verbose = False)   # Hide "Send 1 packets" message on console
    return True
  except:
    return False
        
def print_custom_menu():
  """Obtain inputs to create custom packet

  Returns: Nil
  """    
  print("************************")
  print("* Custom Packet        *")
  print("************************\n")
  x = False
  while x != True:
    src_addr = input("Enter Source address of Packet: ")
    if re.match(re.compile(r'^www\.[A-Za-z0-9]+\.com$'), src_addr):
      x = True
    else:
      print("Invalid Input")
  x = False
  while x != True:
    src_port = input("Enter Source Port of Packet: ")
    try:
      int(src_port)
    except:
      print("Only Numbers Allowed!")
      continue
    if int(src_port) <= 65536 | int(src_port) >= 0:
      x = True
    else:
      print("Invalid Input")
  x = False
  while x != True:
    dest_addr= input("Enter Destination address of Packet: ")
    if re.match(re.compile(r'^www\.[A-Za-z0-9]+\.com$'), dest_addr):
      x = True
    else:
      print("Invalid Input")
  x = False
  while x != True:
    dest_port= input("Enter Destination Port of Packet: ")
    try:
      int(dest_port)
    except:
      print("Only Numbers Allowed!")
      continue
    if int(dest_port) <= 65536 | int(dest_port) >= 0:
      x = True
    else:
      print("Invalid Input")
  x = False
  while x != True:
    pkt_type = input("Enter Type (T) TCP, (U) UDP, (I) ICMP echo request (T/U/I): ")
    if str(pkt_type) == "T" or str(pkt_type) == "U" or str(pkt_type) == "I":
      x = True
    else:
      print("Invalid Input")

  if pkt_type == "I":
    print("  Note: Port number for ICMP will be ignored")
        
  pkt_data = input("Packet RAW Data (optional, will be \"DISM-DISM-DISM-DISM\" left blank): ")
  if pkt_data == "":
    pkt_data = "DISM-DISM-DISM-DISM"
  
  x = False
  while x != True:
    pkt_count = input("No of Packets to send (1-65535): " )
    try:
      int(pkt_count)
    except:
      print("Only Numbers Allowed!")
      continue
    if int(pkt_count) <= 65535 | int(pkt_count) >= 1:
      x = True
    else:
      print("Invalid Input")
  start_now = input("Enter to Start, Any other to return to main menu: ")

  if start_now != "": 
    return
  count = 0
  for i in range(int(pkt_count)):
    if send_packet(src_addr, src_port, dest_addr, dest_port, pkt_type, pkt_data):
      count  = count + 1

  print(count , " packet(s) sent" )
  exit()

print_custom_menu()