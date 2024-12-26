

def aylana(r):
    PI = 3.14
    aylana = {}
    radius = r
    diametr = r*2
    perimetr = diametr*PI
    yuz = PI*(r**2)
    aylana = {'radius':r,"diametr":diametr,"perimetr":perimetr,"yuz":yuz}
    
    return aylana

rad = int(input("Aylananing radiusini kiriting: "))

print(aylana(rad))

