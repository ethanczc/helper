# Networking
Resource: https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md

### wifi details
`$ sudo nano /etc/wpa_supplicant/wpa_supplicant.conf`
>ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev\
>update_config=1\
>country:SG\
>network={\
>ssid="foo"\
>psk="bar\
>}

### commands
scan wireless networks: `$ sudo iwlist wlan0 scan` \
get current SSID: `$ iwgetid`

### set up static ip
get port name of ethernet port: `$ ifconfig`\
`$ sudo nano /etc/network/interfaces` 
>auto "portname" \
>iface "portname" inet static \
>address "staticip" \
>netmask 255.255.255.0

`$ sudo ifup "portname"`\
check if ip is updated: `$ hostname -I`
