Scan the raspberry pi i2c bus to see the addresses of all connected devices.

`sudo apt-get install python-smbus`\
`sudo apt-get install i2c-tools`

Run\
`sudo i2cdetect -y 1`\
Port 1 is for all older raspberry pi versions
