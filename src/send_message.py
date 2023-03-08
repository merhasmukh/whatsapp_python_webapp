
import pywhatkit
import pandas as pd 
import numpy as np
from src import exception
# hour=23
# minutes=33
# data=pd.read_excel("./FARMERS LIST SHREE FARMERS LIST.xlsm")

# print(data.columns)

def send_sms(mob_number,text,hr,mn):
    try:
        print(mob_number)
        print(type(mob_number))
        pywhatkit.sendwhatmsg(mob_number,
                      text,
                      int(hr),int(mn))
    except Exception as e:
        raise exception.CustomException(str(e))

# h=0
# m=1
# for i in data['mo']:
#     print(i)
#     if pd.isna(i):
#         continue
#     else:
#         print("+91"+str(int(i)))


#         pywhatkit.sendwhatmsg("+91"+str(int(i)),
#                       "hi",
#                       hour,minutes)