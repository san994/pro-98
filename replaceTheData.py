def swapFileData():
    file1 = input('enter the first file: ')
    file2 = input('enter the second file: ')

    f1 = open(file1,'r') 
    file1_data = f1.read()
    f2 = open(file2,'r') 
    file2_data = f2.read()

    file1_wrt = open(file1,'w')
    file1_wrt.write(file2_data)

    file2_wrt = open(file2,'w')
    file2_wrt.write(file1_data)

    

swapFileData()