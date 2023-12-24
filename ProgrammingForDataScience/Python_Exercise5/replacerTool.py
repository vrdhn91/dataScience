import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("fileName", help = "File name", type=str)
parser.add_argument("-p", "--pattern", help = "Pattern to be found in the file", default = ',', required=False)
parser.add_argument("-r", "--replace", help = "String to replace the pattern", default= ';', required=False)
parser.add_argument("-o", "--out", help = "Output file", default='', required=False)
parser.add_argument("-fo", "--force", help = "Overwrite flag")
args = parser.parse_args()

inputFileName = os.path.basename("C:\\Users\\vevit\\Documents\\DS_Workspace\\ProgrammingForDataScience\\Exercise5\\text.txt")
splitFileName = os.path.splitext("C:\\Users\\vevit\\Documents\\DS_Workspace\\ProgrammingForDataScience\\Exercise5\\text.txt")
listData =[]

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

listData = parse_csv(args.fileName, ',',0)

new_content = ''
for x in listData:
    tmpStr = x[0]
    new_content += tmpStr.replace(args.pattern,args.replace)

if args.out !='':
    newFileName = args.out+splitFileName[1]
else:
    newFileName= inputFileName.split('.')[0] +'_mod' + splitFileName[1]    

os.listdir('C:\\Users\\vevit\\Documents\\DS_Workspace\\ProgrammingForDataScience\\Exercise5')
files = [f for f in os.listdir() if os.path.isfile(f)]

if newFileName in files and args.force=='0':
    print('Error: Output file has already existed')
else:
    with open(newFileName, "w") as out:
        out.write(new_content)
        print('Output file has been successfully created: ', newFileName)

