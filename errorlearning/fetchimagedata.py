import wget

filecontent = wget.download(r"http://10.252.217.173:8000/test.txt")
print("m here 1")
print(filecontent)
while(true):
    with open(filecontent) as fc :
        print("m here")
        x = fc.read()
        fc.close()
        print(x)
