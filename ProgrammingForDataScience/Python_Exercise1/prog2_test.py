#Write a python program that is called with a variable number of arguments that prints
# all symbols appearing in some arguments together with their counts
# all arguments (i.e. words) appearing at least twice

import sys

word_list = sys.argv
loop_word = 1
dict_arg ={}
    
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
        total_word = 0
    loop_word+=1
    
print(dict_arg)