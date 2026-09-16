def candle_hours(x, y):
    hours = 0
    remains = 0
    
    while x > 0:        #10>0               #3>0            #4>0            #5>0            #7>0
        hours += x       #0+10=10            #10+3=13        #13+4=17        #17+5=22        #22+7=29
        remains += x     #0+10=10            #10+3=13        #13+4=17        #17+5=22        #22+7=29
        
        x = remains // y #10//3=3            #13//3=4        #17//3=5        #22//3=7        #29//3=9
        remains = remains % y #10%3=1           #13%3=1         #17%3=2         #22%3=1         #29%3=2
        
    return hours

print(candle_hours(10,3))







