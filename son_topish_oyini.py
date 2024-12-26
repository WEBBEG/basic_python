import random as r

def son_top(x):
    
    son = r.sample(range(1,x+1),1)[0]
    
    print(f'Men 1 dan {x} oralig\'idagi sonni o\'yladim.')
    sanoq=1
    while True:
        topish = int(input("Men o'ylagan sonni topib ko'ring: "))
        
        if son == topish:
            print(f"Tabriklaymiz, siz sonni topdingiz. Ha, men {son} ni o'ylagan edim.")
            print(f"Siz {sanoq} urinishda topdingiz.")
            break
       
        elif son>topish:
            print(f"Men o'ylagan son {topish} dan katta")
            sanoq= sanoq + 1
        else:
            print(f"Men o'ylagan son {topish} dan kichkina")
            sanoq= sanoq + 1
    return sanoq
def topaman(x):
    print(f"Iltimos 1 dan {x} oralig'idagi hohlagan sonni o'ylang.")
    past = 1
    yuqori = x
    sanoq=1
    input("Boshlash uchun istalgan tugmani bosing")
   
    while True:
        son = r.randint(past, yuqori)
        print(f"Siz {son} ni o'yladingiz")
        j=input("Agar to'g'ri bo'lsa (t), agar xato bo'lsa siz o'ylagan son men aygan {son} dan katta bo'lsa (+), kichik bo'lsa (-) qo'ying ")
        if j == 't':
            print(f"Men {sanoq} urinishda topdim.")
            break
        
        elif j=='+':
            past = son + 1
            sanoq= sanoq + 1
        else:
            yuqori = son - 1
            sanoq= sanoq + 1    
    return sanoq

top = son_top(10)
t_man = topaman(10)
if top>t_man:
    print("Musobaqada men yutdim")
elif top==t_man:
    print("Durrang")
else:
    print("Musobaqada siz yutdingiz")