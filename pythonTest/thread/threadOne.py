#!/usr/bin/python3

import _thread
import threading
import time

# 为线程定义一个函数
def print_time( threadName, delay):
   count = 0
   while count < 20:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

# 创建两个线程
try:
   _thread.start_new_thread( print_time, ("Thread-1", 6, ) )
   _thread.start_new_thread( print_time, ("Thread-2", 10, ) )

except:
   print ("Error: 无法启动线程")


while 1:
   pass

