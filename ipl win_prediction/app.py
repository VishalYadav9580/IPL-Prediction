import streamlit as st
import pickle
import pandas as pd
teams = [
    'Rajasthan Royals', 'Royal Challengers Bangalore','Sunrisers Hyderabad', 'Delhi Capitals', 'Chennai Super Kings',
    'Gujarat Titans', 'Lucknow Super Giants', 'Kolkata Knight Riders','Mumbai Indians', 'Kings XI Punjab']
cities=['Ahmedabad', 'Kolkata', 'Mumbai', 'Navi Mumbai', 'Pune', 'Dubai',
       'Sharjah', 'Abu Dhabi', 'Delhi', 'Chennai', 'Hyderabad',
       'Visakhapatnam', 'Chandigarh', 'Bengaluru', 'Jaipur', 'Indore',
       'Bangalore', 'Raipur', 'Ranchi', 'Cuttack', 'Dharamsala', 'Nagpur',
       'Johannesburg', 'Centurion', 'Durban', 'Bloemfontein',
       'Port Elizabeth', 'Kimberley', 'East London', 'Cape Town']

pipe=pickle.load(open('pipe.pkl','rb'))
st.title('IPL Win Predictor')
col1,col2=st.columns(2)
with col1:
      BattingTeam=st.selectbox('Select the batting team',sorted(teams))

with col2:
    BowlingTeam = st.selectbox('Select the Bowling team', sorted(teams))

selected_city=st.selectbox('Select host city',sorted(cities))

target=st.number_input('Target')

col3,col4,col5=st.columns(3)

with col3:
    score=st.number_input('Score')

with col4:
    overs=st.number_input('Overs Completed')

with col5:
    wicket=st.number_input('Wickets out')

if st.button('Predict_probability'):
    run_left=target-score
    ball_left=120-(overs*6)
    wicket=10-wicket
    crr=score/overs
    rrr=(run_left*6)/ball_left

    input_df = pd.DataFrame(
        {'BattingTeam': [BattingTeam], 'BowlingTeam': [BowlingTeam], 'City': [selected_city], 'run_left': [run_left],
         'ball_left': [ball_left], 'wicket': [wicket], 'total_run_x': [target], 'crr': [crr], 'rrr': [rrr]})

    result=pipe.predict_proba(input_df)
    lose=result[0][0]
    win=result[0][1]
    st.header(BattingTeam+"-"+str(round(win*100))+"%")
    st.header(BowlingTeam + "-" + str(round(lose*100)) + "%")
