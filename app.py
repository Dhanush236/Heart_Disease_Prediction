#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pickle
import streamlit as st
import numpy as np
pickle_in=open('MYhdpapp.pkl','rb')
clf=pickle.load(pickle_in)

def main():
    html_temp='''
    <div style="background-color:yellow;padding:13px">
    <h1 style="color:black;text-align:center;">CORONARY HEART DETECTION PREDICTION</h1>
    </div>'''

    st.markdown(html_temp,unsafe_allow_html=True)
    age=st.number_input("AGE")
    sex=st.number_input("SEX")
    bp=st.number_input('BP')
    cpt=st.number_input("CHEST PAIN TYPE")
    c=st.number_input('CHOLESTEROL')
    fbs=st.number_input('FBS OVER 120')
    ekg=st.number_input('EKG RESULTS')
    hr=st.number_input('MAX HEART RATE')
    ea=st.number_input('EXERCISE ANGINA')
    std=st.number_input('ST DEPRESSION')
    sst=st.number_input('SLOPE OF ST')
    n=st.number_input('NUMBER OF VESSELS FLORO')
    t=st.number_input('THALLIUM')
    result=''

    if st.button('PREDICT'):
        result=prediction(age,sex,bp,cpt,s,fbs,ekg,hr,ea,std,sst,n,t)
        st.success('RISK IS {}'.format(result))

def prediction(age,sex,bp,cpt,s,fbs,ekg,hr,ea,std,sst,n,t):
    s=clf.predict([[age,sex,bp,cpt,s,fbs,ekg,hr,ea,std,sst,n,t]])
    if s==1:
        p='PRESENCE'
    else:
        p='ABSENCE'
    return p

if __name__=='__main__':
    main()
#Age	Sex	Chest pain type	BP	Cholesterol	FBS over 120	EKG results	Max HR	Exercise angina	ST depression	Slope of ST	Number of vessels fluro	Thallium	Heart Disease




