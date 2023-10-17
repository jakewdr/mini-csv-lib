def csvToList(path):
    """Converts CSV to list and outputs it.

    Args:
        path (string): The path of the CSV file

    Returns:
        List: The CSV in list form
    """
    columnCount = int(0); columnNames = []; csvFile = []; count = int(0)
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
            csvFile.append(columnNames)
            
        else:
            values = []
            for i in range(0,columnCount):
                    value = line.split(",")[i]
                    values.append(value.strip())
            csvFile.append(values)
    return csvFile

def specificValue(column,row,path):
    """Returns a specific value from a CSV table

    Args:
        column (int): The column in which the value is located
        row (int): The row in which the value is located
        path (str): The path of the CSV file

    Returns:
        str: String of the requested location, this can be converted.
    """
    csvList = csvToList(path)
    value = csvList[row][column]
    return value

def app(list,path):
    """Appends a list to the end of a CSV file.

    Args:
        list (list): The list to be appended to the CSV file
        path (str): The path of the CSV file
    """
    delim = ", "
    res = '' 
    for ele in list:
        res = res + str(ele) + delim
    file1 = open(path,"a")
    file1.write("\n" + res[:-2])
    file1.close()