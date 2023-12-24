import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("fileName", help = "File name", type=str)
parser.add_argument("-p", "--pattern", help = "Pattern to be found in the file", default = ',', required=False)
parser.add_argument("-r", "--replace", help = "String to replace the pattern", default= ';', required=False)
parser.add_argument("-o", "--out", help = "Output file", default='', required=False)
parser.add_argument("-fo", "--force", help = "Overwrite flag")
args = parser.parse_args()

inputFileName = os.path.basename(args.fileName)
splitFileName = os.path.splitext(args.fileName)

#Arrange the output file
if args.out !='':
    newFileName = args.out+splitFileName[1]
else:
    newFileName= inputFileName.split('.')[0] +'_mod' + splitFileName[1]

#Read directory and get all the filename within the same directory
os.listdir('C:\\Users\\vevit\\Documents\\DS_Workspace\\ProgrammingForDataScience\\Exercise5')
files = [f for f in os.listdir() if os.path.isfile(f)]

#Validate the filename whether filename has existed or not
if newFileName in files and args.force=='0':
    print('Error: Output file has already existed')
else:
    listData = readFile(args.fileName)
    new_content = listData.replace(args.pattern,args.replace) #replace content
    with open(newFileName, "w") as out: #write output file
        out.write(new_content)
        print('Output file has been successfully created: ', newFileName)

#Function to open and read the files
def readFile(fileName):
    textFile = ''
    with open(fileName, 'r') as file:
        for data in file:
            textFile.append(data)
    return textFile
