import requests
import json


def geolocate(ip_address):
  # Use a geolocation database to find the geographic location of the IP address
  geolocation_database = 'https://ipinfo.io/'

  # Make a request to the geolocation database
  response = requests.get(geolocation_database + ip_address)

  # Parse the JSON response
  response_json = response.json()

  # Print the geolocation information
  print('IP Address:', ip_address)
  print('Country:', response_json['country'])
  print('Region:', response_json['region'])
  print('City:', response_json['city'])

  with open('geolocation.txt', 'a') as f:
    f.write(ip_address + ' ' + response_json['country'] + ' ' + response_json['region'] + ' ' + response_json['city'] + '\n')

def vulnerability_scan(ip_address):
  # Add a vulnerability scanner
  vulnerability_scanner = 'nmap'

  # Run the vulnerability scanner
  vulnerability_scanner_results = vulnerability_scanner + ' -sV ' + ip_address

  # Print the results of the vulnerability scan
  print('Vulnerability scan results:')
  print(vulnerability_scanner_results)

  with open('vulnerability_scan.txt', 'a') as f:
    f.write(vulnerability_scanner_results + '\n')


while True:

 #print a menu of options
 print ('''
 1. Geolocate
 2. Vulnerability scan
 3. Both Scans
 4. Change IP (Coming soon)
 5. Change HWID
 6. Quit
 ''')

 #Get users choice
 choice = input('Enter your choice: ')
 
 #checks for users choice
 if choice == '1' or choice =='2':
   ip_address = input('Enter the IP Address: ')
 if choice == '1':
  geolocate(ip_address)
 elif choice == '2':
    vulnerability_scan(ip_address)
 elif choice == '3':
    geolocate(ip_address)
    vulnerability_scan(ip_address)
 elif choice == '4':
    change_ip_address()
 elif choice == '5':
  change_hwid()
 elif choice == '6':
  break
 else:
   print('Invalid Choice')

if choice == '1' or choice =='2':
      with open('ip_addresses.txt', 'a') as f:
        f.write(ip_address + '\n')