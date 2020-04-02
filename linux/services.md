# Running a script as a service
Resource: https://www.freedesktop.org/software/systemd/man/systemd.service.html

### creating the service file
you may or may not choose the following options.\
`/home/pi $ sudo nano myscript.service`

[Unit]\
Description=My service\
After=network.target

[Service]\
ExecStart=/usr/bin/python3 -u pythonscript.py\
WorkingDirectory=/home/pi\
StandardOutput=inherit\
StandardError=inherit\
Restart=always\
RestartSec=3\
User=pi

[Install]\
WantedBy=multi-user.target

`sudo cp myscript.service /etc/systemd/system/myscript.service`

### systemctl commands
`$ systemctl start myscript.service`\
`$ systemctl stop myscript.service`\
`$ systemctl enable myscript.service`\
`$ systemctl status myscript.service`

### logs
`$ journalctl -u myscript.service`

### updating a service file
`$ systemctl daemon-reload` \
`$ restart myscript.service`

### services running in background
`$ service --status-all`\
`$ systemctl list-units -t service`\
`$ systemctl list-units -t service -all`\
or target your service application\
`$ systemctl is-active "applicationName".service`\
`$ systemctl status "applicationName".service`
