#Write a python program that reads a csv file and:
# for every column computes the min, max, mean, median and variance
# writes a new csv file containing the summary statistics (see example file for output
#format)
#You can expect that the input file contains only numeric columns, has no missing values and
#a header row.

import math

listData =[]
with open('iris.num.only.csv', 'r') as file:
    for data in file:
        listData.append(data.rstrip())
        
total_column = len(listData[0].split(','))
header = listData[0].split(',')

#split data each row and convert to float
counter_row = 1
new_data_collection = []
min_value = []
max_value= []
sum_value = []
median_value = []
mean_value = []
variance_value = []

#find min, max, and sum value for the data collection. sum will be used later to find variance
while counter_row < len(listData):
    dataRow = listData[counter_row].split(',')
    counter_column = 0
    newRow = []
    while counter_column < total_column:
        if len(min_value) < total_column:
            min_value.append(dataRow[counter_column])
        else:
            if dataRow[counter_column] < min_value[counter_column]:
                min_value[counter_column] = dataRow[counter_column]
        if len(max_value) < total_column:
            max_value.append(dataRow[counter_column])
        else:
            if dataRow[counter_column] > max_value[counter_column]:
                max_value[counter_column] = dataRow[counter_column]
        if len(sum_value)< total_column:
            sum_value.append(float(dataRow[counter_column]))
        else:
            sum_value[counter_column] += float(dataRow[counter_column])
        newRow.append(float(dataRow[counter_column]))
        counter_column+=1
    new_data_collection.append(newRow)
    counter_row+=1     

#find median value
median_index = 0
if len(new_data_collection) % 2 == 1:
    median_index = math.ceil(len(new_data_collection)/2)
    median_value = new_data_collection[median_index]
else:
    median_index = math.floor(len(new_data_collection)/2)
    x=0
    while x < total_column:
        median_value.append((new_data_collection[median_index-1][x] + new_data_collection[median_index][x])/2)
        x+=1

#find mean value for variance
y=0
while y < total_column:
    mean_value.append(sum_value[y]/len(new_data_collection))
    y+=1;

#def my_function():

counter_row1 = 0
temp_variance = []
while counter_row1 < len(new_data_collection):
    counter_col1 = 0
    variance =[]
    while counter_col1 < len(new_data_collection[counter_row1]):
        variance.append((new_data_collection[counter_row1][counter_col1] - mean_value[counter_col1])**2)
        counter_col1+=1
    temp_variance.append(variance)
    counter_row1+=1
    

index_loop= 0
while index_loop < total_column:
    total = 0
    var = 0
    while var < len(temp_variance):
        total += temp_variance[var][index_loop]
        var+=1
    total= total/(len(new_data_collection)-1)
    variance_value.append(total);    
    index_loop+=1
    

#write into the files
with open("iris_output.txt", "w") as out:
    out.write('colname,min,max,mean,median,variance\n')
    row = 0
    while row < total_column:
        out.write(header[row]+","+str(min_value[row])+","+str(max_value[row])+","+
        str(mean_value[row])+","+str(median_value[row])+","+str(variance_value[row])+'\n')
        row+=1
print('Output file: iris_output.txt')

