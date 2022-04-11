from time import sleep
import os

while True:
  os.system('curl http://www.baidu.com')
  print("i am sleeping...")
  sleep(60*30)
