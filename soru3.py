
sayi=int(input("Lütfen 2 basamaklı bir tam sayı giriniz:"))

for i in range(1,sayi+1):
    if i<10:
        if int(i)%2==1:
            TekSayılar=open("teksayılar.txt","a",encoding="utf-8")
            TekSayılar.write(str(i)+"\n")
        elif int(i)%2==0:
            print(i,"çift olduğu için yazdırılmadı")
    elif i>10 and i<100:
        basamak1=i//10
        basamak2=int(i)-(basamak1*10)
        toplam=basamak1+basamak2
        if toplam%2==1:
            TekSayılar2=open("teksayılar.txt","a",encoding="utf-8")
            TekSayılar2.write(str(i)+"\n")

        elif toplam%2==0:
            print(i,"çift olduğu için yazdırılmadı")