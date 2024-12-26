
def talabalar(ism,familiya,**malumotlar):
    malumotlar['ism']=ism
    malumotlar['familiya']= familiya
    return malumotlar
 
talaba1 = talabalar('arslonbek', 'bekjanov', t_yil='1998')

print(talaba1)
