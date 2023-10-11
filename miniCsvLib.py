def csvToDict (path):
    columnCount = int(0); columnNames = []; csvFile = {}; count = int(0)
    file=open(path,'r')
    read = file.readlines()
    rows = len(read)   
    for i in range (0,rows):
        line = read[i] # Reads the line of the for loops index
        if i == 0:
            for i in line: # This for loop counts the number of columns for later use
                if i == ',': 
                    columnCount = columnCount + 1
            columnCount = columnCount + 1
            for i in range(0,columnCount):
                    columnName = line.split(",")[i]
                    columnNames.append(columnName.strip())
            csvFile["titleRow"] = columnNames
            count = count + 1
        else:
            values = []; count = count + 1
            for i in range(0,columnCount):
                    value = line.split(",")[i]
                    values.append(value.strip())
            name = "row" + str(count-1)
            csvFile[name] = values
    return csvFile

def csvToList(path):
    columnCount = int(0); columnNames = []; csvFile = []; count = int(0)
    file=open("dummy.csv",'r')
        
    read = file.readlines()
    rows = len(read)
        
    for i in range (0,rows):
        line = read[i] # Reads the line of the for loops index
        if i == 0:
            for i in line: # This for loop counts the number of columns for later use
                if i == ',': 
                    columnCount = columnCount + 1
            columnCount = columnCount + 1
            for i in range(0,columnCount):
                    columnName = line.split(",")[i]
                    columnNames.append(columnName.strip())
            csvFile.append(columnNames)
            
        else:
            values = []
            for i in range(0,columnCount):
                    value = line.split(",")[i]
                    values.append(value.strip())
            csvFile.append(values)
    return csvFile

def specificValue(column,row,path):
    csvList = csvToList(path)
    value = csvList[row][column]
    return value
