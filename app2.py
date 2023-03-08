
import pywhatkit
import pandas as pd 
import numpy as np
hour=23
minutes=33
data=pd.read_excel("./FARMERS LIST SHREE FARMERS LIST.xlsm")

print(data.columns)

# pywhatkit.sendwhatmsg("+918000536979",
#                       "Geeks For Geeks!",
#                       22,39)
h=0
m=1
# for i in data['mo']:
#     print(i)
#     if pd.isna(i):
#         continue
#     else:
#         print("+91"+str(int(i)))


#         pywhatkit.sendwhatmsg("+91"+str(int(i)),
#                       "hi",
#                       hour,minutes)