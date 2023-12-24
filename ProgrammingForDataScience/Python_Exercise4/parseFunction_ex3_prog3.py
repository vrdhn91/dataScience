listData =[]
#with open('phone_book.csv', 'r') as file:
#    for data in file:
#        listData.append(data.rstrip().split(','))

header=[]
def parse_csv(fileName, separator, hasHeader):
    lists = []
    global header
    with open(fileName, 'r') as file:
        for data in file:
            row = []
            if hasHeader == 0 or len(header)!=0: 
                row += data.rstrip().split(separator)
                lists.append(row)
            elif hasHeader == 1 and len(header) == 0:
                header += data.rstrip().split(separator)
            else: break
    return lists

listData = parse_csv('phone_book.csv', ',',1)

print(listData)
        
surnameSet = set(listData[x][1].strip('"') for x in range(len(listData)))
forenameSet = set(listData[x][2].strip('"') for x in range(len(listData)))

print('Surname Set:',surnameSet, '\n\n\n')
print('Forename Set', forenameSet, '\n\n\n')

#All names that appear as surname and forename
print('Names appear as surname and forename:', surnameSet.intersection(forenameSet), '\n\n\n')

#All names that appear as surname or forename
#print('Name in surname or forename:', surnameSet.intersection(forenameSet), '\n\n\n')
print('Names appear as surname or forename:',surnameSet.union(forenameSet), '\n\n\n')

#All names that are either only a surname or only a forename
print('Names that are either only a surname or only a forename:',surnameSet.symmetric_difference(forenameSet), '\n\n\n')

#All surnames that are not also a forename
print('Surnames that are not also a forename:',surnameSet.difference(forenameSet), '\n\n\n')