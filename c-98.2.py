
def swappingFiles(f1,f2):
    f1 = open("fileA.txt")
    f2 = open("fileB.txt")

    print("the data stored in files is:\n")
    
    '''
    print(f1.read())
    print(f2.read())
    '''
    data_A = f1.read()
    data_B = f2.read()

    
    print(data_A)
    print(data_B)
    

    f1.close()
    f2.close()

    f1 = open("fileA.txt","w+")
    f1.write(data_B)

    f2 = open("fileB.txt","w+")
    f2.write(data_A)

    f1.close()
    f2.close()

    f1 = open("fileA.txt")
    f2 = open("fileB.txt")

    print("the data after swapping in files is:\n")
    print(f1.read())
    print(f2.read())

    f1.close()
    f2.close()

f1fA = open("fileA.txt")
f2fB = open("fileB.txt")
swappingFiles(f1fA,f2fB)
f1fA.close()
f2fB.close()
