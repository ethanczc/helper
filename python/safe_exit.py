''' clean way to safely exit a while loop using ctrl-c, or terminated from systemctl.
'''
from datetime import datetime
import signal
import time

run_flag = True

def shut_down(signum, frame):
    global run_flag
    now = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    sig_enum = signal.Signals(signum)
    write_str = f'signal caught at {now} with signal {sig_enum}\r\n'
    with open('file.txt', 'w') as f:
        f.write(write_str)
    run_flag = False

signal.signal(signal.SIGINT, shut_down)
signal.signal(signal.SIGTERM, shut_down)

while run_flag:
    print('Doing work..')
    time.sleep(1)

# ------- operational -------------

import signal
run_flag = True

def shut_down(signum, frame):
    global run_flag
    print('Close sockets, ports, etc.')
    run_flag = False

signal.signal(signal.SIGINT, shut_down)
signal.signal(signal.SIGTERM, shut_down)

while run_flag:
    print('Doing work..')