# !/bin/python3

import datetime
import time
import scrollphathd
print('Binary clock is running. Press ctrl-c to stop.')
while True:
    now = datetime.datetime.now()
    bhour = bin(now.hour)[2:].zfill(6)
    bmin = bin(now.minute)[2:].zfill(6)
    bsec = bin(now.second)[2:].zfill(6)
    pos = 0
    for x in bhour:
        if x == '0':
            bright = 0.2
        else:
            bright = 1.0
        scrollphathd.fill(bright,x=pos,y=0,width=2,height=2)
        pos = pos + 3
    pos = 0
    for x in bmin:
        if x == '0':
            bright = 0.2
        else:
            bright = 1.0
        scrollphathd.fill(bright,x=pos,y=3,width=2,height=2)
        pos = pos + 3
    pos = 0
    for x in bsec:
        if x == '0':
            bright = 0.2
        else:
            bright = 1.0
        scrollphathd.fill(bright,x=pos,y=6,width=2,height=1)
        pos = pos + 3
    scrollphathd.show()
    time.sleep(1)
