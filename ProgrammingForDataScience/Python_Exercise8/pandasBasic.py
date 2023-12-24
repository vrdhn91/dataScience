import numpy as np
import pandas as pd

personList = [{'first_name': 'Anthony', 'last_name': 'Gie', 'phone': '17689011', 'zip_code': '10110', 'age': 26, 'height': 170, 'weight': 80},
                {'first_name': 'Benjamin', 'last_name': 'Ho', 'phone': '30509056', 'zip_code': '10189', 'age': 31, 'height': 158, 'weight': 50},
                {'first_name': 'Charlie', 'last_name': 'Xin', 'phone': '21182002', 'zip_code': '10190', 'age': 45, 'height': 163, 'weight': 72},
                {'first_name': 'Douglas', 'last_name': 'Jo', 'phone': '8301925', 'zip_code': '19011', 'age': 25, 'height': 178, 'weight': 85},
                {'first_name': 'Ethan', 'last_name': 'Ken', 'phone': '19472913', 'zip_code': '10109', 'age': 32, 'height': 166, 'weight': 62},
                {'first_name': 'Fiona', 'last_name': 'Lu', 'phone': '63581018', 'zip_code': '16071', 'age': 44, 'height': 155, 'weight': 55}]
                
person_df = pd.DataFrame(personList) 
print(person_df)


#1. Get the first name, last name and age (in this order) for all persons younger than 28.
#data[data['density'] > 100]
temp1 = person_df[person_df['age']<28]
print('Younger than 28: \n', temp1[['first_name', 'last_name', 'age']], '\n')

#2. Get the last name, first name, height, age (in this order) for all persons younger than
#28 AND taller than 175 cm.
temp2 = person_df[((person_df['age']<28) & (person_df['height']>175))]
print('Younger than 28 and taller than 175 cm: \n', temp2[['first_name', 'last_name', 'height','age']], '\n')

#3.One year has passed, time to update your table! Increment the age of all persons by
#one year.
person_df['age'] = person_df['age'] + 1
print('Increased age: \n', person_df)

#4. Add a new column (bmi) to your DataFrame which contains the body mass index
#calculated from the height and weight for each person.
#formula: weight/((height/100)^2)
person_df['bmi'] = person_df['weight']/((person_df['height']/100)**2)
print('Data with BMI: \n',person_df,'\n')

#5. Berlin’s zip codes are in the range 10115 - 14199. Return first name, last name and
#zip code for all persons that appear to live in Berlin.
temp5 = person_df[((person_df['zip_code'].astype('int')<=14199) & (person_df['zip_code'].astype('int')>=10115))]
print('All people who live in Berlin: \n', temp5[['first_name', 'last_name', 'zip_code']])