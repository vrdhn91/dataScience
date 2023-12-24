import numpy as np

#A leap year is each year that is a multiple of 4 (except for years that are a multiple of 100
#but not of 400). Given a NumPy array of integers (years) compute:
#• The number of leap years.
#• The largest and smallest leap year.
#• (only) The leap years sorted in reverse (descending) order.]

#The number of leap years.
years = np.arange(1600,1801)
print('Years range: \n', years, '\n')
noOfLeapYear = years[(years%4==0)]
removeYear = noOfLeapYear[(noOfLeapYear%100==0) & (noOfLeapYear%400!=0)]
leapYear = [x for x in noOfLeapYear if x not in removeYear]
print('The number of leap year: ', len(leapYear),'\n')


#The largest and the smallest years
min = np.min(leapYear)
print('The smallest leap year: ', min)
max = np.max(leapYear)
print('The biggest leap year: ', max, '\n')

#The leap years sorted in reverse (descending) order.]
print('Leap year in descending order: \n', leapYear[::-1])