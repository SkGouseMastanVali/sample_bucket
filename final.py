import stat
import os.path,time
import datetime
from configparser import ConfigParser
import logging

#l_f=[]

#To get all the files in a specific path
#path= r"C:\Users\gmvsh\Desktop\tasks"
logging.basicConfig(filename="log.txt",level=logging.INFO)
logging.info("checking the path")
config = ConfigParser()

try:
  
    config.read('config.ini')
    path=config.get('main','path')
    print(path)

    for root,dirs,files in os.walk(path):
        for i in files:
            #l_f.append(os.path.join(root,i))
            #print(l_f)
            

            file_status=os.stat(os.path.join(root,i)).st_ctime
            now = time.time()
            #print(now)
            file_compare = now - (1 * 86400) 
            if file_status < file_compare:
                print(i)
                
        
#----------------------------------------------------

except NameError as e:
    print("Something went wrong while getting the path")
    logging.exception(e)

logging.info("operation completed")

