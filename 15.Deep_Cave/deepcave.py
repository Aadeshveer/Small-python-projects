import random
import time

WIDTH = 50
PAUSE_AMT = 0.2

print(" Deep Cave ".center(WIDTH,'*'))
print("Press ctrl+C to stop...")
left_gap = random.randint(1,WIDTH//2)
gap = random.randint(2,WIDTH//5)
while(True):
    try:
        right_gap=WIDTH-gap-left_gap
        print('#'*left_gap+' '*gap+'#'*right_gap)
        roll1 = random.randint(1,6)
        if roll1==1 and left_gap>1:
            left_gap-=1
        elif roll1==2 and right_gap>1:
            left_gap+=1
        else:
            pass
        roll2 = random.randint(1,6)
        if roll2==1 and gap>1:
            gap-=1
        elif roll2==2 and right_gap>1:
            gap+=1
        time.sleep(PAUSE_AMT)
    except KeyboardInterrupt:
        print("\nSo you quit before reaching the bottom, You might never know what lies beneath the caves.")
        break