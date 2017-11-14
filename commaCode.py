import copy

def listtostr(inputList):
    inputLength=len(inputList)
    copiedList=copy.copy(inputList)
    for i in range(1,inputLength):
        if i < (inputLength-1):
            copiedList[0]=str(copiedList[0])+', '+str(copiedList[i])
            i=i+1
        else:
            copiedList[0]=str(copiedList[0])+', and '+str(copiedList[i])
    liststr=copiedList[0]
    print(liststr)
