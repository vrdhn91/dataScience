listData =[]
with open('phone_book.csv', 'r') as file:
    for data in file:
        listData.append(data.rstrip().split(','))
   
#1. all unique forenames separately for females and males (if gender can be inferred from title entry).   
titleMaleTupl = ('mr','mr.')
titleFemaleTupl = ('ms', 'mrs','mrs.', 'ms.', 'miss')

setNameMale = set(listData[x][2].strip('"') for y in range(len(listData[0])) if y == 3 for x in range(len(listData)) if listData[x][y].lower() in titleMaleTupl)
print('Male Name:', setNameMale, '\n\n')

setNameFemale = set(listData[x][2].strip('"') for y in range(len(listData[0])) if y == 3 for x in range(len(listData)) if listData[x][y].lower() in titleFemaleTupl)
print('Female Name:', setNameFemale, '\n\n')

#2. all entries (complete rows) for persons where forename and surname are longer than 8 characters.
listLongerThanEight = [listData[x] for x in range(len(listData)) if len(listData[x][1]) > 8 and len(listData[x][2])>8]
print('Data people with both firstname and lastname longer than 8 chars:', listLongerThanEight, '\n\n')

#3.all surnames (unique) containing more vowels than consonants
vowelsTup = ('a','i','u','e','o')
setSurname = set(surname[1] for surname in range(len(listData)) for char in list(surname[1]) if char in vowelsTup countVowels+=1 else countConsonant+=1 if countVowels > countConsonant)
print(setSurname)