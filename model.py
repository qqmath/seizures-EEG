import matplotlib.pyplot as plt
import pandas as pd
import joblib



base = '/Users/adityavs14/Documents/Internship/Pianalytix/Month_2/EEgSeizure/app'
model = joblib.load(f'{base}/svmeeg.joblib')
df = pd.read_csv(f'{base}/Epileptic Seizure Recognition.csv')
df = df.drop(columns = df.columns[0]) 



def predict(data):
    new_input1 = [df.iloc[data, :177]]
    
    new_output = model.predict(new_input1)
    if new_output==[1]:
        s = 'yes you might get seizure be conscious about it'
    else:
        s = 'You are safe no worries :)'
    return s
