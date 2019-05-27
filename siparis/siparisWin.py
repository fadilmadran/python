#!/usr/bin/python

import os , sys
import time

currentDir = os.getcwd()
libDir = os.path.dirname(currentDir)
#libDir = os.path.join("C:/", "Users", "fmadran", "Desktop", "FADIL", "myProjects", "python")
directory = os.path.join(currentDir, "Siparisler")
sys.path.append(libDir)
import util

tarih = util.getDate()

menuDosya = os.path.join(libDir, "siparis", "menu.txt")

suFiyat          = 1 #1 TL
cayFiyat         = 2 #2 TL
turkKahvesiFiyat = 4 #4 TL
kupaKahveFiyat   = 6 #6 TL
sogukKahveFiyat  = 7 #7 TL
sutluTatliFiyat  = 8 #8 TL
baklavaFiyat     = 9 #9 TL
pastaFiyat       = 7 #7 TL

urunSayisi       = 8


def fiyatGuncelle():
        global suFiyat, cayFiyat, turkKahvesiFiyat, kupaKahveFiyat, sogukKahveFiyat, sutluTatliFiyat, baklavaFiyat, pastaFiyat
        print("Fiyat Guncelle")
        if os.path.exists(menuDosya):
                os.chmod(menuDosya, 666)
                os.remove(menuDosya)

        suFiyat = raw_input("Su:")
        cayFiyat = raw_input("Cay:")
        turkKahvesiFiyat = raw_input("Turk Kahvesi:")
        kupaKahveFiyat = raw_input("Latte/Mocha:")
        sogukKahveFiyat = raw_input("Buzlu Kahve:")
        sutluTatliFiyat = raw_input("Sutlu Tatli:")
        baklavaFiyat = raw_input("Baklava:")
        pastaFiyat = raw_input("Pasta:")

        fMenu = open(menuDosya, 'a+')
        fMenu.write("Su:" +  suFiyat + "\n")
        fMenu.write("Cay:" +  cayFiyat + "\n")
        fMenu.write("Turk Kahvesi:" +  turkKahvesiFiyat + "\n")
        fMenu.write("Latte/Mocha:" +  kupaKahveFiyat + "\n")
        fMenu.write("Buzlu Kahve:" +  sogukKahveFiyat + "\n")
        fMenu.write("Sutlu Tatli:" +  sutluTatliFiyat + "\n")
        fMenu.write("Baklava:" +  baklavaFiyat + "\n")
        fMenu.write("Pasta:" +  pastaFiyat)
        fMenu.write("\n")
        fMenu.close()
        os.chmod(menuDosya, 444)
        menuDosyasiniOku()


def menuDosyasiniOku():
        if not os.path.exists(menuDosya):
                print("Menu dosyasi bulunamadi!")
                return

        fMenu = open(menuDosya, 'r')
        menuLst = fMenu.read().split('\n')
        print("\n")
        for urun in menuLst:
                print(urun)
        print("\n\n")
        urunSayisi = len(menuLst)

        bekle = raw_input("Devam etmek icin bir tusa basiniz:")


def urunEkle():
        if not os.path.exists(menuDosya):
                print("Lutfen once menu dosyasini olusturunuz!")
                return

        yeniurunAdi = raw_input("Urun Adi:")
        yeniUrunFiyat = raw_input("Fiyat:")
        #urunSayisi = urunSayisi + 1
        fMenu = open(menuDosya, 'a+')
        fMenu.write(yeniurunAdi + ":" + yeniUrunFiyat)
        fMenu.write("\n")
        fMenu.close()
        menuDosyasiniOku()


def menuIslem():
        print("Henuz yapim asamasinda!");
        return ;
        menuChoice = raw_input("  1.Mevcut Menu\n  2.Fiyat Guncelle\n  3.Urun ekle\n")
        try:
                val = int(menuChoice)
                if val == 1:
                        menuDosyasiniOku()
                elif val == 2:
                        fiyatGuncelle()
                elif val == 3:
                        urunEkle()
                else:
                        print("Gecersiz Secim")
        except ValueError:
                print("line: 100 Bir hata olustu")



def siparisEkrani():
        order_list = []
        masa = raw_input("Masa No:")
        while masa == "":
            masa = raw_input("Lutfen bir masa numarasi giriniz:")

        su = raw_input("Su:")
        if su == "":
                su = "0"
        cay = raw_input("Cay:")
        if cay == "":
                cay = "0"
        turkKahvesi = raw_input("Turk Kahvesi:")
        if turkKahvesi == "":
                turkKahvesi = "0"
        kupaKahve = raw_input("Latte/Mocha:")
        if kupaKahve == "":
                kupaKahve = "0"
        sogukKahve = raw_input("Buzlu Kahve:")
        if sogukKahve == "":
                sogukKahve = "0"
        sutluTatli = raw_input("Sutlu Tatli:")
        if sutluTatli == "":
                sutluTatli = "0"
        baklava = raw_input("Baklava:")
        if baklava == "":
                baklava = "0"
        pasta = raw_input("Pasta:")
        if pasta == "":
                pasta = "0"

        onay = raw_input("Onayla:'Enter' / iptal:'i'")
        if not onay == "":
            print("\nSiparis girilmedi!")
            return order_list

        try:
                val=int(masa)
                val=int(su)
                val=int(cay)
                val=int(turkKahvesi)
                val=int(kupaKahve)
                val=int(sogukKahve)
                val=int(sutluTatli)
                val=int(baklava)
                val=int(pasta)
        except ValueError:
                print("line:132 Bir hata olustu!!!")
                return order_list

        order_list.append(su)
        order_list.append(cay)
        order_list.append(turkKahvesi)
        order_list.append(kupaKahve)
        order_list.append(sogukKahve)
        order_list.append(sutluTatli)
        order_list.append(baklava)
        order_list.append(pasta)
        order_list.append(masa)
        return order_list


def eskiSiparis(filename):
        os.chdir(os.path.join(directory, tarih))
        file = open(filename, 'r+')
        line_lst = file.readlines()
        file.close()

        su              = line_lst[1][0]
        cay             = line_lst[2][0]
        turkKahvesi     = line_lst[3][0]
        kupaKahve       = line_lst[4][0]
        sogukKahve      = line_lst[5][0]
        sutluTatli      = line_lst[6][0]
        baklava         = line_lst[7][0]
        pasta           = line_lst[8][0]

        eski_siparis_lst = []
        eski_siparis_lst.append(su)
        eski_siparis_lst.append(cay)
        eski_siparis_lst.append(turkKahvesi)
        eski_siparis_lst.append(kupaKahve)
        eski_siparis_lst.append(sogukKahve)
        eski_siparis_lst.append(sutluTatli)
        eski_siparis_lst.append(baklava)
        eski_siparis_lst.append(pasta)
        os.remove(filename)
        return eski_siparis_lst


def siparisYaz():
        eski_sipars_lst = []
        yeni_lst = []
        last_lst = []
        siparisler = siparisEkrani()
        if len(siparisler) != 9:
                return 0

        filename = "Masa" + str(siparisler[len(siparisler)-1])
        if os.path.exists(os.path.join(directory, tarih, filename)) :
                eski_sipars_lst = eskiSiparis(filename)
                yeni_lst.append(int(siparisler[0]) + int(eski_sipars_lst[0])) #su
                yeni_lst.append(int(siparisler[1]) + int(eski_sipars_lst[1])) #cay
                yeni_lst.append(int(siparisler[2]) + int(eski_sipars_lst[2])) #turkKahvesi
                yeni_lst.append(int(siparisler[0]) + int(eski_sipars_lst[3])) #kupaKahve
                yeni_lst.append(int(siparisler[1]) + int(eski_sipars_lst[4])) #sogukKahve
                yeni_lst.append(int(siparisler[2]) + int(eski_sipars_lst[5])) #sutluTatli
                yeni_lst.append(int(siparisler[0]) + int(eski_sipars_lst[6])) #baklava
                yeni_lst.append(int(siparisler[1]) + int(eski_sipars_lst[7])) #pasta
                last_lst = yeni_lst
        else :
                last_lst = siparisler

        os.chdir(os.path.join(directory, tarih))
        f = open(filename, 'a+')
        f.write("Saat = " + str(util.getTime()))
        f.write("\n")
        i = 0
        toplam = 0
        for miktar in last_lst :
                if str(miktar) == "" :
                        miktar = 0
                if i == 8:
                        break
                if i == 0 :
                        tur = " su  "
                        fiyat = suFiyat
                elif i == 1 :
                        tur = " cay"
                        fiyat = cayFiyat
                elif i == 2 :
                        tur = " turkKahvesi"
                        fiyat = turkKahvesiFiyat
                elif i == 3 :
                        tur = " kupaKahve"
                        fiyat = kupaKahveFiyat
                elif i == 4 :
                        tur = " sogukKahve"
                        fiyat = sogukKahveFiyat
                elif i == 5 :
                        tur = " sutluTatli"
                        fiyat = sutluTatliFiyat
                elif i == 6 :
                        tur = " baklava"
                        fiyat = baklavaFiyat
                else :
                        tur = " pasta"
                        fiyat = pastaFiyat
                i = i + 1
                toplam = toplam + int(int(miktar) * fiyat)
                f.write(str(int(miktar)) + tur + " = " + str(int(miktar) * fiyat) + "   TL")
                f.write("\n")
        f.write("Toplam  = " + str(toplam) + " TL")
        f.write("\n")
        f.close()
        print("Siparis onaylandi")


def siparisGir():
        siparisYaz()
        return 0


def masaAktar():
        print("Masa Aktar")
        eski_masa = raw_input("Eski Masa:")
        while eski_masa == "":
            eski_masa = raw_input("Lutfen bir masa numarasi giriniz:")

        try:
                val = int(eski_masa)
        except ValueError:
                print("line:276 Bir hata olustu")
                return 0

        os.chdir(os.path.join(directory, tarih))
        if not os.path.exists("Masa" + str(eski_masa)):
                print("Masa bulunamadi")
                time.sleep(1)
                return 0

        yeni_masa = raw_input("Yeni Masa:")
        while yeni_masa == "":
            yeni_masa = raw_input("Lutfen bir masa numarasi giriniz:")

        try:
                val = int(yeni_masa)
        except ValueError:
                print("line:269 Bir hata olustu")
                time.sleep(1)
                return 0

        if os.path.exists("Masa" + str(yeni_masa)):
                print("Masa %d'nin  hesabi kapatilmadi" %int(yeni_masa))
                time.sleep(1)
                return 0

        os.rename("Masa" + str(eski_masa), "Masa" + str(yeni_masa))
        print("Masa%s Masa%s'ye aktarildi." %(eski_masa, yeni_masa))
        time.sleep(1)
        return 0


def hesabiOde(masa_no, odemeTuru):
        os.chdir(os.path.join(directory, tarih))
        f = open("Masa" + str(masa_no), 'a+')
        f.write(odemeTuru)
        f.write("\n")
        f.close()
        os.rename("Masa" + str(masa_no), str(util.getTime()) + "_OdendiMasa" + str(masa_no))


def hesapKapat(masa_no):
        os.chdir(os.path.join(directory, tarih))
        filename = "Masa" + str(masa_no)
        if not os.path.exists(filename) :
                print("Masa bulunamadi!!!")
                time.sleep(1)
                return 0
        else :
                file = open(filename, 'r+')
                print("Hesap:\n%s" %file.read())
                file.close()
                odemeTuru = "bos"
                while True:
                        odemeSekli = raw_input("1.Nakit\n2.Kredi Karti\n")
                        if odemeSekli == "1":
                                odemeTuru = "Nakit"
                                break
                        elif odemeSekli == "2":
                                odemeTuru = "Kredi Karti"
                                break
                        else:
                                continue
                
                kapat = raw_input("Hesabi kapat:'Enter' / Iptal:'i':")
                if str(kapat) == "" :
                        hasilatHesapla(masa_no, odemeTuru)
                        hesabiOde(masa_no, odemeTuru)
                else :
                        print("Hesap kapanmadi!")
                        time.sleep(1)
                        return 0
        
        print("Hesap Kapandi")
        time.sleep(1)
        return 0


def acikMasalar():
        dirLst = os.listdir(os.path.join(directory, tarih))
        dirLst.sort()
        cntr = 0
        for dosya in dirLst :
                if dosya[0] == "M" :
                        cntr = cntr + 1

        if cntr == 0 :
                print("\nAcik masa yok!")
        else :
                print("\nAcik masalar:")
                for dosya in dirLst :
                        if dosya[0] == "M" :
                                print(dosya)

        return 0


def toplamHasilataYaz(masaNo, hesapTutari, odemeTuru):
        # once dokum satirini duzenliyoruz. Masa icin 10, saat icin 15, odeme turu icin 15 karakter olacak
        odenenMasa = "Masa" + str(masaNo)
        odemeSaati = str(util.getTime())
        if len(odemeSaati) == 3:
                odemeSaati = "0" + odemeSaati

        odemeSaati = odemeSaati[:2] + ":" + odemeSaati[2:] # convert ssdd to ss:dd

        for i in range(10 - len(odenenMasa)):
                odenenMasa = odenenMasa + " "

        for i in range(15 - len(odemeSaati)):
                odemeSaati = odemeSaati + " "

        for i in range(15 - len(odemeTuru)):
                odemeTuru = odemeTuru + " "

        dokumSatiri = odenenMasa + odemeSaati + odemeTuru + str(hesapTutari) + " TL"
        
        os.chdir(os.path.join(directory, tarih))
        f = open("Hasilat_Dokumu", 'a+')
        #f.write("Masa" + str(masaNo) + " = " + str(hesapTutari) + " TL")
        f.write(dokumSatiri)
        f.write("\n")
        f.close()

        f1 = open("Toplam_Hasilat", 'a+')
        hasilat = int(f1.read())
        f1.close()
        os.remove("Toplam_Hasilat")

        f2 = open("Toplam_Hasilat", 'a+')
        f2.write(str(int(hesapTutari) + hasilat))
        f2.close()
        

def hasilatHesapla(masa_no, odemeTuru):
        os.chdir(os.path.join(directory, tarih))
        f = open("Masa" + str(masa_no), 'r+')
        line_lst = f.readlines()
        f.close()
        
        length = len(line_lst)
        son_satir = line_lst[length-1] # "Toplam = x TL"
        tutar = son_satir.split("=")[1] # "x TL"
        fiyat = tutar.split(" ")[1] # "x"
        hesapTutari = int(fiyat) # convert "x" to integer x
        print("Hesap Tutari:%d" %hesapTutari)
        
        toplamHasilataYaz(masa_no, hesapTutari, odemeTuru)


def gunSonuHasilat():
        os.chdir(os.path.join(directory, tarih))
        f = open("Toplam_Hasilat", 'r+')
        print("\nToplam Hasilat : %s TL" %f.read())
        f.close()

        return 0


def hasilatDokumu():
        os.chdir(os.path.join(directory, tarih))
        f = open("Hasilat_Dokumu", 'r+')
        hasilat_lst = f.readlines()
        f.close()
        print("Hasilat Dokumu:\n\n")
        for hasilat in hasilat_lst :
                print(hasilat)


def initDirs():
        util.createDir(directory)
        os.chdir(directory)
        util.createDir(tarih)
        os.chdir(tarih)
        if not os.path.exists(os.path.join(directory, tarih, "Hasilat_Dokumu")) :
                f = open("Hasilat_Dokumu", 'a+')
                # once dokum satiri icin basligi duzenliyoruz. Masa icin 10, saat icin 10, odeme turu icin 12 karakter olacak
                f.write("Masa No   Odeme Saati    Odeme Turu     Tutar\n")
                f.write("----------------------------------------------")
                f.write("\n")
                f.close()
        
        if not os.path.exists(os.path.join(directory, tarih, "Toplam_Hasilat")) :
                f1 = open("Toplam_Hasilat", 'a+')
                f1.write("0")
                f1.close()


def main():
        while True:
                time.sleep(0.5)
                #os.system("clear")
                print("\n" * 60)
                if not os.path.exists(menuDosya):
                        raw_input("Menu olusturmaniz gerekmektedir.\nDevam etmek icin bir tusa basiniz")
                        fiyatGuncelle()


                print("\n1.Siparis Gir\n2.Masa Aktar\n3.Masa Hesap\n4.Acik Masalar\n5.Gun Sonu Hasilat\n6.Gun Sonu Hasilat Dokumu\n7.Menu Islemleri\n8.Cikis\n")
                choice = raw_input("Seciminiz:")
                try:
                        val = int(choice)
                        initDirs()
                        if val == 1:
                                siparisGir()
                        elif val == 2:
                                masaAktar()
                        elif val == 3:
                                masa_no = raw_input("Masa No:")
                                try:
                                        valMasa = int(masa_no)
                                        hesapKapat(valMasa)
                                except ValueError:
                                        print("line:488 Bir hata olustu")
                                        return 0
                        elif val == 4:
                                acikMasalar()
                                enter = raw_input("\nDevam etmek icin bir tusa basin")
                        elif val == 5:
                                gunSonuHasilat()
                                enter = raw_input("\nDevam etmek icin bir tusa basin")
                        elif val == 6:
                                hasilatDokumu()
                                enter = raw_input("\nDevam etmek icin bir tusa basin")
                        elif val == 7:
                                menuIslem()
                        elif val == 8:
                                break
                        else :
                                print("Gecersiz Secim!!!")
                except ValueError:
                        continue
                        #print "line: 491 Girdiginiz karakter bir sayi degil!!!"


        return 0


if __name__ == "__main__":
        main()
