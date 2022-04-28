def searchEnd(massNum, index):#поиск конца индекса икомого элемента
    end = index
    ask = 0
    flag = False
    while flag != True:
        if len(massNum)+1 == end+1 or massNum[index] != massNum[end]:
            ask = end
            flag = True
        else:
            end += 1
    return ask

def searchStart(massNum, index):#поиск начала индекса искомого элемента
    start = index
    flag = False
    ask = 0
    while flag != True :
        start -= 1
        if start < 0 or massNum[index] != massNum[start]:
            ask = start+2
            flag = True
    return ask


def searchAllElement(massNum, index):#получение индексов элементов
    if index not in inData: # если искомый элемент на присутствует в словаре
        endRes = searchEnd(massNum,index)   # то происходит нахождение его
        startRes = searchStart(massNum, index) # индексов и запись их в словарь
        inData[index] = (endRes, startRes)
    file.write(str(inData[index][1])+' '+str(inData[index][0])+'\n')   # вывод итоговых значаний



def search_data(massNum, request, search):#поиск индексов значений
    for i in range(int(request)):
        l = -1
        r = len(massNum)
        flag = True
        while r > l+1:
            m = int((l+r)/2)
            if massNum[m] < search[i]:
                l = m
            else:
                r = m
            if massNum[m] == search[i]:
                searchAllElement(massNum, m)
                flag = False
                break
        if flag:
            file.write('-1 ' + '-1' + '\n')
    return

def main():
    with open('input.txt', 'r', encoding = 'utf8') as inputFile:
        count = inputFile.readline().strip()
        massNum = list(map(int,inputFile.readline().split()))
        request = inputFile.readline().strip()
        search = list(map(int,inputFile.readline().split()))
    search_data(massNum, request, search)

if __name__ == '__main__':
    inData = {}
    file = open('output.txt', 'w', encoding = 'utf8')
    main()
    file.close()