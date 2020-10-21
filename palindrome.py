def pali(str2):
    str2=str2.upper()
    
    if str2==str2[::-1]:        #compairing with reverse of string
        out="String is Palindrome"
    else:
        out="String is not a Palindrome"
        
    return out

in_str2=input("\nEnter String to check palindrome: ")
print(pali(in_str2))
