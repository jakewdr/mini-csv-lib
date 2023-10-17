import miniCsvLib as mcl
path = "dummy.csv"

print(mcl.csvToList(path))
print(mcl.specificValue(1,1,path))
mcl.app(["one","two","three"], "dummy.csv")
