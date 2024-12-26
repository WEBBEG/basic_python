
def f_yasa(ism,familiya,t_yil,yosh,t_joy,email='',t_raqam=''):
    foydalanuvchi = {
        "ism":ism,
        "familiya":familiya,
        "t_yil":t_yil,
        "t_joy":t_joy,
        "email":email,
        "t_raqam":t_raqam,
        "yosh":yosh
        }
    return foydalanuvchi

print("Foydalanuvchi qo'shing")

mijozlar = []

while True:
    ism = input("Mijozning ismini kiriting ")
    familiya = input("Mijozninig familiyasini kiriting ")
    yosh = int(input("yoshini kirgazing "))
    t_yil = input("Tug'gilgan yilini kiriting ")
    t_joy = input("Tug;ilgan joyini kiriting ")
    email = input("Emailni kiriting ")
    t_raqam = input("Telefon raqam kiriting ")
    
    talaba1 =
    
    savol = input("Yana mijoz qo'shasizmi? (ha/yo'q) ")
    
    
    mijozz.append(f_yasa(ism, familiya, t_yil, yosh, t_joy,email,t_raqam))
    
    if savol == "yo'q":
        break
    

print(mijozlar)