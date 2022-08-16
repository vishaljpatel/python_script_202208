import os
import subprocess
import datetime

dt = datetime.datetime.now()
dir_name = dt.strftime("%Y%m%d_%H%M%S")
dir_name ="sswrp_"+dir_name 
#print(dir_name)

cmd_rt=subprocess.run(["pwd"], check=True, stdout=subprocess.PIPE, text=True)
pwd=cmd_rt.stdout
pwd=pwd.strip() #removes \n from left & right side of string
dir_name_abs=pwd+"/"+dir_name
print(dir_name_abs)
