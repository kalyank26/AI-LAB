def multi_table(num,k):
    for i in range(k):
        ans=num*(i+1)
        print(f'{num}*(i+1)={ans}')

table=int(input("enter the number\n"))
k=int(input('till which number\n'))
multi_table(table,k)