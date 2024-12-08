

# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']

# for car in cars:
#     if car != 'gm':
#         print(car.title())
#     else :
#         print(car.upper())


# - Foydalanuvchi login ismini so'rang. Agar login `admin` bo'lsa, `"Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?"` xabarini konsolga chiqaring. 
# foydalanuvchi_ismi = input('Login:')

# if foydalanuvchi_ismi.lower() == 'admin':
#     print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print("Xush kelibsiz, {foydalanuvchi_ismi}!")

# - Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, `"Sonlar teng"` ekan degan yozuvni konsolga chiqaring.

# sonlar = []

# sonlar.append(input('1-chi sonni kiriting'))
# sonlar.append(input('2-chi sonni kiriting'))

# if sonlar[0]==sonlar[1]:
#     print('Sonlar teng')


# - Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga `"Manfiy son"`, agar musbat bo'lsa `"Musbat son"` degan xabarni chiqaring. 

son = int(input("Iltimos, istalgan sonni kiriting \n>>"))
if son >0:
    print('Musbat son')
    print(son**0.5)
else: 
    print ('Musbat sonni kiriting')



    
# - Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, `"Musbat son kiriting"` degan xabarni chiqaring. 