import csv
with open ("c:\Users\Mr.Chow\Desktop\test\text.csv",newline=' ') as f:
    reader=csv.reader(f)
    for i in reader:
        print(i)