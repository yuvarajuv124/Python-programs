a,b,c,d,e = 10,20,3,40,50
def highest(a,b,c,d,e):
    if(a>b and a>c and a>d and a>e):
        print('Highest number is:',a)
    elif(b>c and b>d and b>e):
        print('Highest number is:',b)
    elif(c>d and c>e):
        print('Highest number is:',c)
    elif(d>e):
        print('Highest number is:',d)
    else:
        print('Highest number is:',e)
    #print('Highest number is:',max(a,b,c,d,e))
def lowest(a,b,c,d,e):
    if(a<b and a<c and a<d and a<e):
        print('Lowest number is:',a)
    elif(b<c and b<d and b<e):
        print('Lowest number is:',b)
    elif(c<d and c<e):
        print('Lowest number is:',c)
    elif(d<e):
        print('Lowest number is:',d)
    else:
        print('Lowest number is:',e)
    #print('Lowest number is:',min(a,b,c,d,e))
highest(a,b,c,d,e)
lowest(a,b,c,d,e)
