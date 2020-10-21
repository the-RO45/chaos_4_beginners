def freq(str1):
    str1=str1.replace(" ","")
    fr_dct={}
    for i in str1:
        fr_dct[i]=fr_dct.get(i,0)+1    #counts occurance of character in string
        
    mkey=0
    m=0
    for key,value in fr_dct.items():
        if(value >m):
            m=value       #character
            mkey=key    #occurance
    return mkey
in_str=input("Enter String: ")
print("Frequent character is",freq(in_str))
