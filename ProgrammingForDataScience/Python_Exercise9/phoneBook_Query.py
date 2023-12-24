import numpy as np
import pandas as pd
from Levenshtein import distance as levenshtein_distance

name = input('name:')
maxError = int(input('maxError: '))
onlyWithPhone = bool(input('onlyWithPhone: '))

fileName = "phone_book.csv"
data_csv = pd.read_csv(fileName,sep=",", usecols = ['SURNAME','FORENAME', 'TITLE', 'PHONE', 'EMAIL'])

data_csv['SurnameDist'] = [levenshtein_distance(i, name) for i in data_csv['SURNAME']]
#data_csv['ForenameDist'] = [levenshtein_distance(i, name) for i in data_csv['FORENAME']]

#print(data_csv.info())
test = data_csv[(data_csv.FORENAME.astype(str))!=data_csv.FORENAME]
data_csv['FORENAME'] = data_csv['FORENAME'].fillna('')
data_csv['ForenameDist'] = [levenshtein_distance(i, name) for i in data_csv['FORENAME']]

pplWithMaxErr = data_csv[(((data_csv['SURNAME']== name) | (data_csv['FORENAME']==name)) & ((data_csv['SurnameDist'] == maxError) | (data_csv['ForenameDist'] == maxError)))]
print('All entries match with name and the most Levenshtein distance: \n',pplWithMaxErr, '\n')

#If onlyWithPhone is True only entries with phone numbers should be reported.
if onlyWithPhone == True:  
    pplWithMaxErr = pplWithMaxErr.dropna(subset=['PHONE'])
print('All with phone parameter ', onlyWithPhone, ': \n',pplWithMaxErr)

#Entries should be sorted in ascending order according to SURNAME, FORENAME and PHONE.
print('Ascending order based on SURNAME, FORENAME and PHONE: \n',pplWithMaxErr.sort_values(by=['SURNAME','FORENAME','PHONE']))