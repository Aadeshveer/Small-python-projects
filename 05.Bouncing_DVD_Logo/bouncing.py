import sys
import random
import time
import bext

message = 'DVD'
num_logos = 5
color = [random.choice(['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']) for _ in range(num_logos)]
delta_x = [random.choice([-2,-1,1,2]) for _ in range(num_logos)]
delta_y = [random.choice([-2,-1,1,2]) for _ in range(num_logos)]
X,Y = bext.size()
x = [random.randint(1,X-1) for _ in range(num_logos)]
y = [random.randint(1,Y-1) for _ in range(num_logos)]
bext.hide_cursor()
i=0
while(i<100):
    for j in range(num_logos):
        bext.goto(x[j],y[j])
        bext.fg(color[j])
        print(message)
        x[j]+=delta_x[j]
        y[j]+=delta_y[j]
        if x[j]<0 or x[j]>=X-len(message):
            x[j]-=2*delta_x[j]
            delta_x[j] = -delta_x[j]
        if y[j]<0 or y[j]>=Y:
            y[j]-=2*delta_y[j]
            delta_y[j] = -delta_y[j]
    time.sleep(0.2)
    bext.clear()
    i+=1
bext.show_cursor()