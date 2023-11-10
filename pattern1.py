def pattern1(num):
    for i in range(1,num+1):
        for j in range(i):
            print(f"{i},",end=' ')
        print("\n")

num=int(input("enter the number\n"))
pattern1(num)
