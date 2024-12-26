

def finabon (a):
    f=[1,1]
    for n in range(a-2):
        f.append(f[-1]+f[-2])
       
        
    
    
    return f

print(finabon(30))


