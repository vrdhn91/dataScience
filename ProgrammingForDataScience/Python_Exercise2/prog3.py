#Write a python program that reads a text file and returns all words in the file that are
#palindromes together with their occurence count. The palindrome check should be case
#insensitive!

text_file = ''
with open('palindrome.txt', 'r') as file:
    for data in file:
        text_file += data.rstrip()
words = text_file.split(' ')

dict_result = {}
for word in words:
    if word not in dict_result and word == word[::-1]:
        dict_result[word] = 1
    elif word in dict_result and word == word[::-1]:
        dict_result[word] +=1
        
print(dict_result)