class ClipList(list):
    
    def __init__(self, number, inputList, min,max):
        self.min = min
        self.max = max
        self.number = number
        self.inputList = inputList
    
    def append(self, number, index):
        tmp = [number]
        self.inputList = self.inputList + tmp
        return self.inputList
        
    
    def extend(self):
        print('')
        
    def __setitem__(self, number):
        self.number = number
        return self.number


inputNo = ''

numberList = []
cl = ClipList(inputNo, [],0,0)
counter = 0
try:
    while inputNo != 0:
        inputNo = int(input('Insert a number: '))
        if len(numberList) == 0:
            numberList = cl.append(inputNo,counter)
            cl.min = inputNo
            cl.max = inputNo
        elif inputNo > cl.max:
            cl.max = cl.__setitem__(inputNo)
            numberList = cl.append(inputNo,counter)
            print('Max number clipped: ', cl.max)
        elif inputNo < cl.min:
            cl.min = cl.__setitem__(inputNo)
            numberList = cl.append(inputNo,counter)
            print('Min number clipped: ', cl.min)
        counter+=1
except ValueError:
    print('Exit')
    
print(numberList)
    




