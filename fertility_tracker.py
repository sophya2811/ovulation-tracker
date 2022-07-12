import streamlit as st
import datetime
from datetime import timedelta, date
from PIL import Image
st.title('OVULATION AND PERIOD TRACKER')
st.markdown('## **Track Your Time**')
st.text('This App is designed to track periods and ovulation, increase your chances and help \nyou understand your unique partern')
date=st.date_input('Enter your last period date')
cycle=st.slider('select your period cycle',21,45)
peak_ovulation=round(cycle*0.5)
next_period=date + timedelta(days=cycle)
most_fertile=date + timedelta(days=peak_ovulation)
sex_date=most_fertile-timedelta(days=2)
if st.button('See Your Ovulation/Most Fertile Date And Your Next Period'):
    st.success(f'your ovulation and most fertile date is {most_fertile}')
    st.error(f'you are adviced to meet with your spouse on {sex_date}')
    st.success(f'your next period is {next_period}')
st.sidebar.image('P Tracker.jpeg')    
st.sidebar.write('Welcome to ovulation and period tracker app')
st.sidebar.markdown('## **how Can we be of service**')
if st.sidebar.button('CLICK HERE FOR MORE INFO'):
    help_list=['SPEAK WITH A CONSULTANT','KNOW YOUR CYCLE']
    st.sidebar.radio('Select',help_list)
        
