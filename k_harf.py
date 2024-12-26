
def katta(matnlar):
    k_matnlar = []
    while matnlar:
        k_matnlar.append(matnlar.pop().title())

        
    return k_matnlar


m = ["qanday zo'r","eh bu yoshligim", "nima gap o'rtoq"]

print(katta(m[:]))

print(m)