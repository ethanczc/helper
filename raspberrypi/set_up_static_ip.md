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