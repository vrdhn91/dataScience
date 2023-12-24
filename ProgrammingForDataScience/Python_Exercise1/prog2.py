#Write a python program that is called with a variable number of arguments that prints
# all symbols appearing in some arguments together with their counts
# all arguments (i.e. words) appearing at least twice

import sys

# all symbols appearing in some arguments together with their counts
counter = 1
str_symbol = ''
dict_symbol ={}
while counter <= len(sys.argv)-1:
    str_symbol += sys.argv[counter]
    counter += 1

for counter_1 in str_symbol:
    total_char = 0
    count_char = 0
    unique_key = ''
    if counter_1 not in dict_symbol.keys():
        unique_key = counter_1
        while count_char < len(str_symbol): 
            if unique_key == str_symbol[count_char]:
                total_char+=1
            count_char+=1
        dict_symbol[unique_key] = total_char
print(dict_symbol, '\n')


# all arguments (i.e. words) appearing at least twice
word_list = sys.argv
dict_arg ={}
loop_word = 1

print('All words appear at least twice: ')
while loop_word <= len(word_list)-1:
    total_word = 0
    count_word = 1
    unique_key = ''
    if sys.argv[loop_word] not in dict_arg.keys():
        unique_key = sys.argv[loop_word]
        while count_word <= len(word_list)-1: 
            if unique_key == sys.argv[count_word]:
                total_word+=1
            count_word+=1
        dict_arg[unique_key] = total_word
        if total_word >= 2:
            print(unique_key)
    loop_word+=1
    
#print(dict_arg)