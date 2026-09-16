x, y = 0, 0 # start at the origin
seq = input() # up left right stop
while seq != 'STOP':
    if seq == 'UP':
        y += 1 #y=1
    if seq == 'DOWN':
        y -= 1
    if seq == 'LEFT':
        x -= 1 #x=-1
    if seq == 'RIGHT':
        x += 1 #x=0
    seq = input() # stop
    # pow is a built in function
    # pow(x, y) is equivalent to x ** y
    dist = pow(x ** 2 + y ** 2, 0.5)
    # rounding off to two decimal places
print(f'{dist:0.2f}')