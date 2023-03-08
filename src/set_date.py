import datetime 
import streamlit as st

def d_set():
    try:
        today_date=datetime.datetime.now().date().day
        today_month=datetime.datetime.now().month
        today_year=datetime.datetime.now().year
        print(today_date)
        print(type(today_date))

        d = st.date_input("select the date of the mesaage")
        
        st.write('Your Date is:', d)

        # return d
        # if st.button("Set Date"):
        #     st.write('Your Date is:', d)
        #     return d
        # else:
        #     st.error("set date error")

    except Exception as e:
        st.error(str(e))