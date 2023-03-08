
import pywhatkit
import pandas as pd 
import numpy as np
from src import exception


def send_sms(mob_number,text,hr,mn):
    try:
        print(mob_number)
        print(type(mob_number))
        pywhatkit.sendwhatmsg(mob_number,
                      text,
                      int(hr),int(mn))
    except Exception as e:
        raise exception.CustomException(str(e))

