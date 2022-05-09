#https://classroom.udacity.com/courses/ud036

import time
import webbrowser

print("This program start on " + time.ctime())

def breaking(time_sec, total_breaks):
    """timemer open youtube

    Args:
        time_sec (int): จำนวนเวลาที่หยุด
        total_breaks (int): จำนวนครั้งที่ทำงาน
    """
    
    break_count = 0

    while(break_count < total_breaks):
        time.sleep(time_sec)
        webbrowser.open("https://www.youtube.com/watch?v=TfOWv2u0Xvc")
        break_count += 1

breaking(20,2)
