def sol(n):
   #add code here
   if n%3 == 2:
       unit1= int(n//3)
       unit2= int((n-unit1)/2)
   else:
       unit2= int(n//3)
       unit1= int(n - 2*(unit2))
       
   return unit1+unit2

# do not edit below code
def main():
    n=int(input())
    print(sol(n))

if __name__ == '__main__':
    main()