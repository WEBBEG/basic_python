a=int(input("Birinchi sonni kiriting: "))

b=int(input("Ikkinchi sonni kiriting: "))

def katta_son(a,b):
    if a>b:
        print(f"Katta son {a}")
    elif a<b:
        print(f"Katta son {b}")
    else:
        print(f"Ikkala son teng")


katta_son(a,b)