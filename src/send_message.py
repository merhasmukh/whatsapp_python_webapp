
import pywhatkit
import pandas as pd 
import numpy as np
from src import exception
# hour=23
# minutes=33
# data=pd.read_excel("./FARMERS LIST SHREE FARMERS LIST.xlsm")

# print(data.columns)

def send_sms(mob_number):
    try:
        pywhatkit.sendwhatmsg(mob_number,
                      "Geeks For Geeks!",
                      11,45)
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