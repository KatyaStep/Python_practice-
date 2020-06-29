def printTable(data):
    colWidths = [0] * len(data)
    
    for element in range(len(data)):
        max_length = -1
        for item in data[element]:
            if max_length < len(item):
                max_length = len(item)
                colWidths[element] = max_length
                #print(max_length)

    for x in range(len(data[0])):
        for y in range(len(data)):
            print(data[y][x].rjust(colWidths[y]), end = ' ')
        print()
   
    #print("colwidth: ", colWidths)





tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)