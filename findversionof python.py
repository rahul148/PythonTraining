#find the version of your python compiler
import sys
import datetime
print("the version of python")
print(sys.version)
print("the info of version ")
print(sys.version_info)

#print the cureent date and time
now=datetime.datetime.now()
print(now.strftime("\ncurrent date and time\n\n%y-%m-%d  %H:%M:%S"))
