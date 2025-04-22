def q2():
    def upperCase():
        output=''
        tem=0
        string=input("Enter any string:")
        for char in string:
            if 'z'>=char>='a':
                tem=ord(char)
                tem=tem-32
                c=chr(tem)
                output=output+c
            else:
                output=output+char
        print(output)


    def lowercase():
        output=''
        tem=0
        string=input("Enter any string:")
        for char in string:
            if 'A'<=char<='Z':
                tem=ord(char)
                tem=tem+32
                c=chr(tem)
                output=output+c
            else:
                output=output+char
        print(output)
    

    def toggleCase():
        output=''
        tem=0
        string=input("Enter any string:")
        for char in string:
            if 'A'<=char<='Z':
                tem=ord(char)
                tem=tem+32
                c=chr(tem)
                output=output+c
            elif 'z'>=char>='a':
                tem=ord(char)
                tem=tem-32
                c=chr(tem)
                output=output+c
            else:
                output=output+char
        print(output)
    upperCase()
    lowercase()
    toggleCase()
q2()