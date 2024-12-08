
# Foydalanuvchi kiritgan sonni 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz 
# bo'linishini konsolga chiqaring.

butun_son = int(input('Butun son kiriting'))


for son in range(2,11):
    if butun_son%son == 0:
        print(f'{butun_son}  {son} soniga qoldiqsiz bo\'linadi')
        
        