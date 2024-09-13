n=int(input('Number of rows you want.:-'))
for l in range(1,n+1):
    for s in range(1,n-l+1):
        print(' ',end='')
    for a in range(1,2*l):
        print('*',end='')
    print()    
k=input('Press to exit')
