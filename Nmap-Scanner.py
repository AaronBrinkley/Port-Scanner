import nmap





#These variables will be used as ranges for the nmap tool to scan throug
port_min = 0
port_max = 65535

#User types in ip address of device
#ip_address = input("Please enter the IP address for your device")

with open('devices_file') as f:
    devices_list = f.read().splitlines()


#User types in range of ports to be scanned
#port_range = input("Please enter port range in 'x-x' format ")


#Saves port scanner to a variable
nm = nmap.PortScanner()

#Runs a for loop for that prints a message with each IP address from devices_file
for device in devices_list:

    print("Now Checking " + device)

#Port scanner is used on each IP address from devices_file
    for port in range(port_min, port_max + 1):
        try:

            result = nm.scan(device, str(port))
        
            port_status = (result['scan'][device]['tcp'][port]['state'])
            print(f"Port {port} is {port_status}")

        except:
            print("Port {port} is not scannable")