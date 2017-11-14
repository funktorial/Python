tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

#def listLengths(listOfLists):
#    Lengths = [0]*len(listOfLists)
#   for i in range(len(listOfLists)):
#        Lengths[i]=len(tableData[i])
    #print(Lengths)
    

def printTable(tableData):
    colWidths = [0]*len(tableData)
    for i in range(len(tableData)):
        colWidths[i]=len(max(tableData[i]))
    for i in range(len(tableData[0])):
        for j in range(len(tableData)):
            line = ''
            line += tableData[j][i].rjust(colWidths[j])
        print(line)
        
                    
       
    
        
    
