from datetime import datetime
import re

#convert dates in format yyyy-mm-dd to format dd-mm-yyyy.
currDt = datetime.today().strftime('%Y-%m-%d')
pattern = r'(\d{4})(-\d{2}-)(\d{2})'
switch = r'\3\2\1'
newDtFormat = re.sub(pattern, switch, currDt)
print('Convert date to format dd-MM-yyyy: ', newDtFormat,'\n')

#return all integer numbers in a string together with their positions.
text = 'There are 365 days within 1 year and 366 days during the leap year.'
print('Text:', text)
pattern1 = r'\b(\d*?)\b'
for m in re.finditer(pattern1, text):
    if(m.group(1)!=''):
        print('Numbers and their position:', m.group(1), m.start(1), m.end(1))
        
#return all float numbers in a string together with their positions.
text1 = '2,54 cm equals with 1 inch'
print('\nText:',text1)
pattern2 = r'\b((\d*?)([,]+)(\d*))\b'
for m in re.finditer(pattern2, text1):
    if(m.group(1)!=''):
        print('Float and their position:', m.group(1), m.start(1), m.end(1))
        
#convert all snake case words to camelCase.
text2 = 'this_is_a_name_of_an_attribute'
print('\nSnake case:',text2)
pattern3 = r'(([a-z]*)([_])([a-z])([a-z]*))'
result=''
result = re.findall(pattern3, text2)
print(result)
convertToCamel = [list(x) for x in result]
camelCase = ''
for i in convertToCamel:
    tmp = i[3].upper()
    camelCase = camelCase + str(i[1]) + str(tmp) + str(i[4])
print('Camel Case:', camelCase)

#Compressing strings
text3='acccgtaaaaatc'
print('\nText:', text3)
pattern4 = r'((?P<ch>\w)(?P=ch)+)'
for m in re.finditer(pattern4,text3):
    text3 = text3.replace(m.group(1), '{'+str(len(m.group(1)))+'}')
print('Compressed String: ',text3)