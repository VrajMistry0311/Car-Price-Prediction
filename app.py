
import streamlit as st
import joblib
import numpy as np

def main():
    html_temp = """
    <div style="background-color:#ADD8E6;padding:16px">
    <h2 style="color:black";text-align:center> Car price prediction using ML</h2>
    </div>
    
    """
    
    st.markdown(html_temp,unsafe_allow_html=True)
    
    model = joblib.load('model_joblib')
    
    p1 = st.number_input("Enter current car price")
    p2=st.number_input("Enter no. of Kms driven")
    s1 = st.selectbox('Enter owner',(0,1,2))
    p3=st.number_input("How old car is?")
    s2=st.selectbox("Fuel Type",("Diesel","Petrol"))
    s3=st.selectbox("Seller type",("Individual","Dealer"))
    s4=st.selectbox("Transmission type",("Mannual","Automatic"))
    
    
    
    if s2=='Diesel':
        f1=1
        f2=0
    else:
        f1=0
        f2=1
    if s3=='Individual':
        f3=1
    else:
        f3=0
    if s4=="Mannual":
        f4=1
    else:
        f4=0   
    
    if st.button('Predict'):
        pred= model.predict([[p1,p2,s1,p3,f1,f2,f3,f4]])
        
        st.balloons()
        st.success('Your Car Price is {}'.format(round(pred[0],2)))
        
    
    
        
    
    
    
if __name__ == '__main__':
    main()
