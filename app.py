import pandas as pd
import numpy as np
import streamlit as st
import pickle


model=pickle.load(open('model.pkl','rb'))


st.title('Employee Promotion prediction')


department=st.selectbox('Department',('Technology', 'Procurement', 'Analytics', 
                                      'Sales & Marketing','Operations', 'R&D',
                                      'HR', 'Legal', 'Finance'))

region=st.selectbox('Region',(    'region_2', 'region_7', 'region_26', 'region_14', 'region_4',
    'region_31', 'region_22', 'region_11', 'region_15', 'region_13',
    'region_16', 'region_25', 'region_32', 'region_29', 'region_27',
    'region_10', 'region_24', 'region_34', 'region_17', 'region_1',
    'region_8', 'region_12', 'region_19', 'region_6', 'region_28',
    'region_33', 'region_9', 'region_3', 'region_5', 'region_23',
    'region_30', 'region_21', 'region_20', 'region_18'))

education=st.selectbox('Education level',("Bachelor's", "Master's & above", 'Below Secondary'))

gender=st.selectbox('Gender',('f','m'))
recruitment_channel=st.selectbox('Recruitment chanel',('sourcing', 'other', 'referred'))


no_of_trainings=st.number_input('number of trainings taken')

age =st.number_input('employe age')
previous_year_rating =st.number_input('last year rating')

length_of_service=st.number_input('service lenth')
awards_won=st.number_input('number of awards')
avg_training_score=st.number_input('average training score')


data={'department':department,'region':region,
           'education':education,'gender':gender,'recruitment_channel':recruitment_channel,
           'no_of_trainings':no_of_trainings,'age':age,'previous_year_rating':previous_year_rating,
            'length_of_service':length_of_service ,'awards_won?':awards_won,
            'avg_training_score':avg_training_score
}
features=pd.DataFrame(data,index=[0])

user_input=features
prediction=model.predict(user_input)
predict=st.button('Prediction')



if  predict:

    if prediction==1 :
        st.header('Employe will be promoted')
    else:
        st.header('employee will not be promoted')