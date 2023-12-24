#Write a python program that reads a csv file and receives three string arguments
# <agg>: string argument from the set (min, max, mean, sum)
# <gcol>: string defining the grouping column name
# <acol>: string defining the aggregation column name
#Your program will group the rows according to the unique values in the grouping column
#and aggregate the values in the aggregation column according to the provided function. The
#group values together with their aggregation results shall be printed to the command line in
#a two column user friendly format. See example below!

grouped_col = input('Please input grouping column name:')
aggregate_col = input('Please input aggregate column name:')
arg = input('Please input aggregation function:')

path = 'C:\\Users\\vevit\\Documents\\DS_Workspace\\Exercise2\\'

listData =[]
with open(path+'iris.num.only.csv', 'r') as file:
    for data in file:
        listData.append(data.rstrip())

headerName = listData[0].split(',')

a=0
while a < len(headerName):
    if headerName[a] == grouped_col: index_grouped = a
    if headerName[a] == aggregate_col: index_aggregate = a
    a+=1

dict_result = {}
count_occurrence = {}
b = 1
while b < len(listData):
    if arg == 'sum':
        if len(dict_result) == 0 or listData[b].split(',')[index_grouped] not in dict_result:
            dict_result.update({listData[b].split(',')[index_grouped]:float(listData[b].split(',')[index_aggregate])})
        else:
            value = dict_result[listData[b].split(',')[index_grouped]]
            dict_result[listData[b].split(',')[index_grouped]] = float(value)+float(listData[b].split(',')[index_aggregate])
    elif arg == 'min':
        if len(dict_result) == 0 or listData[b].split(',')[index_grouped] not in dict_result:
            dict_result.update({listData[b].split(',')[index_grouped]:listData[b].split(',')[index_aggregate]})
        else:
            value = dict_result[listData[b].split(',')[index_grouped]]
            if listData[b].split(',')[index_aggregate] < value:
                dict_result[listData[b].split(',')[index_grouped]] = listData[b].split(',')[index_aggregate]
    elif arg == 'max':
        if len(dict_result) == 0 or listData[b].split(',')[index_grouped] not in dict_result:
            dict_result.update({listData[b].split(',')[index_grouped]:listData[b].split(',')[index_aggregate]})
        else:
            value = dict_result[listData[b].split(',')[index_grouped]]
            if listData[b].split(',')[index_aggregate] > value:
                dict_result[listData[b].split(',')[index_grouped]] = listData[b].split(',')[index_aggregate]
    elif arg == 'mean':
        #sum
        if len(dict_result) == 0 or listData[b].split(',')[index_grouped] not in dict_result:
            dict_result.update({listData[b].split(',')[index_grouped]:float(listData[b].split(',')[index_aggregate])})
        else:
            value = dict_result[listData[b].split(',')[index_grouped]]
            dict_result[listData[b].split(',')[index_grouped]] = float(value)+float(listData[b].split(',')[index_aggregate])
        #count
        if len(count_occurrence) == 0 or listData[b].split(',')[index_grouped] not in count_occurrence:
            count_occurrence.update({listData[b].split(',')[index_grouped]:1})
        else:
            value = count_occurrence[listData[b].split(',')[index_grouped]]
            count_occurrence[listData[b].split(',')[index_grouped]] = value+1
    b+=1
    
if arg == 'mean':
    for res in dict_result:
        dict_result[res] = dict_result[res] / count_occurrence[res]
print(dict_result)          