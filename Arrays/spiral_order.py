def spiral_order(d:int):
    res=[[0 for i in range(d)] for _ in range(d)]
    print(res)
    shift=((0,1), (1,0), (0,-1),(-1, 0))
    next_x=0
    next_y=0
    direction=x=y=0


    for i in range(1, d**2+1):
        res[x][y]=i
        next_x,next_y= x+shift[direction][0],y+shift[direction][1]
        if(next_x not in range(d) or next_y not in range(d) or res[next_x][next_y]!=0):
            direction=(direction+1)%4
            next_x,next_y= x+shift[direction][0],y+shift[direction][1]
    
        x,y=next_x, next_y
    for j in res:
        print(j)
    
spiral_order(3)