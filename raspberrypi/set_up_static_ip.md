# Raspberry pi set up static ip address
source: https://pimylifeup.com/raspberry-pi-static-ip-address/

- find host network router ip: `ip r | grep default`
- get ip from nameserver: `sudo nano /etc/resolv.conf`
- `sudo nmtui`
- edit host network connection.
- change ipv4 configuration to manual
- enter desired ip to addresses
- enter router ip to gateway
- enter nameserver ip to DNS servers
- select ok, and quit
- `sudo systemctl restart NetworkManager`

## Creating a connection from nmtui
- from existing ssh connection or via monitor
- `sudo nmtui`
- edit a connection
- enter profile name (make it same as ssid for easy reference)
- enter device & mac address eg. wlan0 (2C:CF:67:D0:84:FD)
- enter SSID & password
- do the ipv4 manual configuration as above.