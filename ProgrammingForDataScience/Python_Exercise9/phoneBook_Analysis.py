import numpy as np
import pandas as pd

fileName = "phone_book.csv"
data_csv = pd.read_csv(fileName,sep=",", usecols = ['SURNAME','FORENAME', 'TITLE', 'PHONE', 'EMAIL'])

pd.Series(data_csv.TITLE).value_counts().plot.pie( autopct = "%.2f%%" )

