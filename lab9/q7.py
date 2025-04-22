def ispalindrome():
    string=input("Enter a string value to check:")
    rev=""
    for ele in string:
        rev= ele + rev
        
    if string == rev:
        print("Given string value is palindrome")
    else:
        print("Given string value is not palindrome")
    
ispalindrome()