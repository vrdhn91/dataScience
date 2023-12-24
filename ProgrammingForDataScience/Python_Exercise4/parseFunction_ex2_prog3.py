#Write a python program that reads a text file and returns all words in the file that are
#palindromes together with their occurence count. The palindrome check should be case
#insensitive!

#text_file = ''
#with open('palindrome.txt', 'r') as file:
#    for data in file:
#        text_file += data.rstrip().split(' ')
#words = text_file.split(' ')
path = 'C:\\Users\\vevit\\Documents\\DS_Workspace\\Exercise2\\'
words = []
header = []
def parse_csv(fileName, separator, hasHeader):
    lists = []
    global header
    with open(fileName, 'r') as file:
        for data in file:
            if hasHeader == 0 or len(header)!=0: 
                lists += data.rstrip().split(separator)
            elif hasHeader == 1 and len(header) == 0:
                header += data.rstrip().split(separator)
            else: break
    return lists
    
words = parse_csv(path+'palindrome.txt', ' ',0)

dict_result = {}
for word in words:
    if word not in dict_result and word == word[::-1]:
        dict_result[word] = 1
    elif word in dict_result and word == word[::-1]:
        dict_result[word] +=1
        
print(dict_result)