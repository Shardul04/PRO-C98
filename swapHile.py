def swappingFile():

    Text1=input("Enter File name 1 :-")
    Text2=input("Enter File name 2 :-")
    Text1

    with open(Text1,'r')as a:
        data_a=a.read()

    with open(Text2,'r')as b:
        data_b=b.read()

    with open(Text1,'w')as a:
        a.write(data_b)

    with open(Text2,'w')as b:
        b.write(data_a)


swappingFile()