days=7
for i in range(1,days+1):
    total=0
    rainfall=int(input())
    while(rainfall!=-1):
        total=total+rainfall
        rainfall=int(input())
    print(total)   