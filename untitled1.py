
# birinchi_son = int(input('Birinchi sonni kiriting:'))

# ikkinchi_son = int(input('Ikkinchi sonni kiriting:'))

# if birinchi_son>ikkinchi_son:
#     print(f'{birinchi_son} katta {ikkinchi_son} dan')
# elif ikkinchi_son>birinchi_son:
#     print(f'{birinchi_son} kichkina {ikkinchi_son} dan')
# else:
#     print('Ikkala son bir biriga teng')
    

# mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. 

mahsulotlar =['kartoshka', 'piyoz', 'sabzi', 'go\'sht', 'lovya', 'jo\'xori', 'lavlagi', 'sholg\'om', 'tuxum', 'tvorog']
# Yangi, savat degan bo'sh ro'yxat yarating 
savat = []

bor_mahsulotlar =[]
mavjud_emas = []

for n in range(5):
    savat.append(input(f'Savatga {n+1}chi mahsulotni kiriting'))

for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
        
    else:
        mavjud_emas.append(mahsulot)
if mavjud_emas:
     print(f"Quyidagi mahsulotlar do\'konimizda yo\'q: {mavjud_emas}")
else:
    print('Siz so\'ragan barcha mahsulotlar do\'konimizda bor')
          

# Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabar
# aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.