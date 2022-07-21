import pickle
import pandas as pd
import streamlit as st

from PIL import Image

data=pd.read_csv("data_for_streamlit")

pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

def main():
    # Create a page dropdown
    image = Image.open('image1.jpg')
    st.sidebar.image(image,width=100)
    st.sidebar.title("Insurance Prediction")
    col1, col2 = st.columns( [0.5, 0.5])
    with col1:
        st.title("Insurance prediction")   
    with col2:
       st.image(image,  width=150)
    page = st.sidebar.selectbox("Select One", ['ABOUT',"PREDICTION"])
    if page == "ABOUT":
        st.title('Welcome to Insurance Prediction')
        st.write('Creator Profile:')
        st.write('**Creators:** Ashwin')

    if page == "PREDICTION":
        st.title('PREDICTION')
        age = st.slider("select the Age of the person",int(data.age.min()),int(data.age.max()))
        job = st.selectbox("Select the Occupation ",data.job.unique())
        if job == 'blue-collar':
            grouped=data[data['job']=='blue-collar']
            job = 0
        elif job == 'entrepreneur':
            grouped=data[data['job']=='entrepreneur']
            job = 1
        elif job == 'housemaid':
            grouped=data[data['job']=='housemaid']
            job = 2
        elif job == 'services':
            grouped=data[data['job']=='services']
            job = 3
        elif job == 'technician':
            grouped=data[data['job']=='technician']
            job = 4
        elif job == 'technician':
            grouped=data[data['job']=='unknown']
            job = 5
        elif job == 'self-employed':
            grouped=data[data['job']=='self-employed']
            job = 6
        elif job == 'admin.':
            grouped=data[data['job']=='admin.']
            job=7
        elif job == 'management':
            grouped=data[data['job']=='management']
            job=8
        elif job == 'unemployed':
            grouped=data[data['job']=='unemployed']
            job=9
        elif job == 'retired':
            grouped=data[data['job']=='retired']
            job=10
        elif job == 'student':
            grouped=data[data['job']=='student']
            job=11
        
        education_qual = st.selectbox("Select the Education qualification ",data.education_qual.unique())
        if education_qual == 'primary':
            grouped=data[data['education_qual']=='primary']
            education_qual = 0
        elif education_qual == 'secondary':
            grouped=data[data['education_qual']=='secondary']
            education_qual=1
        elif education_qual == 'unknown':
            grouped=data[data['education_qual']=='unknown']
            education_qual=2
        elif education_qual == 'tertiary':
            grouped=data[data['education_qual']=='tertiary']
            education_qual=3

        call_type = st.selectbox("Select the Call type ",data.call_type.unique())
        if call_type == 'telephone':
            grouped=data[data['call_type']=='telephone']
            call_type = 0
        elif call_type == 'unknown':
            grouped=data[data['call_type']=='unknown']
            call_type=1
        elif call_type == 'cellular':
            grouped=data[data['call_type']=='cellular']
            call_type=2

        day = st.slider("select the day ",int(data.day.min()),int(data.day.max()))
        st.write('**from 0 to 11 is jan to dec')
        mon = st.slider("select the Month ",0,11)
        dur = st.slider("select the Call duration ",int(data.dur.min()),int(data.dur.max()))
        num_calls = st.slider("select the Number of calls made to customer ",int(data.num_calls.min()),int(data.num_calls.max()))


        marital = st.selectbox("Select the Marital status ",data.marital.unique())
        if marital == 'divorced':
            marital_divorced = 1
        else:
            marital_divorced = 0
            
        if marital == 'married':
            marital_married = 1
        else:
            marital_married = 0
        
        if marital == 'single':
            marital_single = 1
        else:
            marital_single = 0
        
        prev_outcome = st.selectbox("Select the Previous Outcome ",data.prev_outcome.unique())
        if prev_outcome == 'failure':
            prev_outcome_failure=1
        else:
            prev_outcome_failure=0

        if prev_outcome == 'other':
            prev_outcome_other=1
        else:
            prev_outcome_other=0
        
        if prev_outcome == 'success':
            prev_outcome_success=1
        else:
            prev_outcome_success=0

        if prev_outcome == 'unknown':
            prev_outcome_unknown=1
        else:
            prev_outcome_unknown=0

        input = pd.DataFrame([[age,job,education_qual, call_type, day, mon, dur,num_calls, marital_divorced,marital_married,marital_single,prev_outcome_failure,prev_outcome_other,prev_outcome_success,prev_outcome_unknown]])


        if st.button("Predict"):
            valu = classifier.predict(input)
            if valu==0:
                st.write('DECLINED')
            else:
                st.write('ACCEPTED')
                st.snow()

        if st.button("About"):
            st.text("Lets Learn")
            st.text("Built with Streamlit")

if __name__=='__main__':
    main()
