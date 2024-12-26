

def tub_top(min,max):
    son = list(range(min,max+1))
    tub = []
    for n in son:
        tub_t = True
        for a in range(2,n):
            if (n%a==0):
                tub_t = False
                
        if tub_t:
                tub.append(n)
    return tub
                    


print(tub_top(2,50))
