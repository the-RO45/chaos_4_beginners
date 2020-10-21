def long_length(str1):
    s=str1.split()
    maxi=0
    for i in s:
        if maxi<len(i):   
            lon_word=i      #i stores longest word
            maxi=len(i)
    return lon_word
in_str=input("Enter String: ")
print("Longest Word is",long_length(in_str))
