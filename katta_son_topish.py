
def k_qaytarish(x,y,z):
    katta = max
    if x==max:
        katta=x
    elif y==max:
        katta=y
    else:
        katta=z
           
    return katta
    
    
    

x = input("x sonni kiriting ")
y = input("y sonni kiriting ")
z = input("z sonni kiriting ")

son = k_qaytarish(x, y, z)



print(f"Eng katta son - {son}")

