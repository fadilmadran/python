#!/usr/bin/python

import os , sys
import time

directory = "/home/ekent/projects/denemeler/python/siparis/Siparisler/"
sys.path.append("/home/ekent/projects/denemeler/python")
import util

tarih = util.getDate()

menuDosya = "/home/ekent/projects/denemeler/python/siparis/menu.txt"

suFiyat 		 = 1 #1 TL
cayFiyat	 	 = 2 #2 TL
turkKahvesiFiyat = 4 #4 TL
kupaKahveFiyat 	 = 6 #6 TL
sogukKahveFiyat  = 7 #7 TL
sutluTatliFiyat  = 8 #8 TL
baklavaFiyat 	 = 9 #9 TL
pastaFiyat 		 = 7 #7 TL

urunSayisi		 = 8


def fiyatGuncelle():
	print "Fiyat Guncelle"
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
	fMenu.close()
	os.chmod(menuDosya, 444)
	menuDosyasiniOku()


def menuDosyasiniOku():
	fMenu = open(menuDosya, 'r')
	menuLst = fMenu.read().split('\n')
	urunSayisi = len(menuLst)


def urunEkle():
	if not os.path.exists(menuDosya):
		print "Lutfen once menu dosyasini olusturunuz!"
		return

	urunAdi = raw_input("Urun Adi:")
	yeniUrunFiyat = raw_input("Fiyat:")
	#urunSayisi = urunSayisi + 1 



def menuDuzenle():
	menuChoice = raw_input("  1.Fiyat Guncelle\n  2.Urun ekle\n")
	try:
		val = int(menuChoice)
		if val == 1:
			fiyatGuncelle()
		elif val == 2:
			urunEkle()
		else:
			print "Gecersiz Secim"
	except ValueError:
		print "line: 83 Girdiginiz karakter bir sayi degil!!!"



def siparisEkrani():
	order_list = []
	masa = raw_input("Masa No:")
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
		print "line:59 Girdiginiz karakter sayi degil!!!"
		return 0

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
	os.chdir(directory + tarih)
	file = open(filename, 'r+')
	line_lst = file.readlines()
	file.close()

	su 			= line_lst[1][0]
	cay 		= line_lst[2][0]
	turkKahvesi = line_lst[3][0]
	kupaKahve 	= line_lst[4][0]
	sogukKahve 	= line_lst[5][0]
	sutluTatli 	= line_lst[6][0]
	baklava 	= line_lst[7][0]
	pasta 		= line_lst[8][0]

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
	if os.path.exists(directory + tarih + "/" + filename) :
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

	os.chdir(directory + tarih)
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
		toplam = toplam + (int(miktar) * fiyat)
		f.write(str(int(miktar)) + tur + " = " + str(int(miktar) * fiyat) + "   TL")
		f.write("\n")
	f.write("Toplam  = " + str(toplam) + " TL")
	f.write("\n")
	f.close()


def siparisGir():
	siparisYaz()
	return 0


def masaAktar():
	print "Masa Aktar"
	eski_masa = raw_input("Eski Masa:")
	try:
		val = int(eski_masa)
	except ValueError:
		print "line:180 Girdiginiz karakter sayi degil"
		return 0

	os.chdir(directory + tarih)
	if not os.path.exists("Masa" + str(eski_masa)):
		print "Masa bulunamadi"
		time.sleep(1)
		return 0

	yeni_masa = raw_input("Yeni Masa:")
	try:
		val = int(yeni_masa)
	except ValueError:
		print "line:193 Girdiginiz karakter sayi degil"
		time.sleep(1)
		return 0

	if os.path.exists("Masa" + str(yeni_masa)):
		print "Masa %d'nin  hesabi kapatilmadi" %int(yeni_masa)
		time.sleep(1)
		return 0

	os.rename("Masa" + str(eski_masa), "Masa" + str(yeni_masa))
	print "Masa%s Masa%s'ye aktarildi." %(eski_masa, yeni_masa)
	time.sleep(1)
	return 0


def hesabiOde(masa_no):
	os.chdir(directory + tarih)
	os.rename("Masa" + str(masa_no), str(util.getTime()) + "_OdendiMasa" + str(masa_no))


def hesapKapat(masa_no):
	os.chdir(directory + tarih)
	filename = "Masa" + str(masa_no)
	if not os.path.exists(filename) :
		print "Masa bulunamadi!!!"
		time.sleep(1)
		return 0
	else :
		file = open(filename, 'r+')
		print "Hesap:\n%s" %file.read()
		file.close()
		kapat = raw_input("Hesabi kapatmak icin 1'e yada 'Enter'a basin:")
		if kapat == 1 or str(kapat) == "" :
			hasilatHesapla(masa_no)
			hesabiOde(masa_no)
		else :
			print "Hesap kapanmadi!"
			time.sleep(1)
			return 0
	
	print "Hesap Kapandi"
	time.sleep(1)
	return 0


def acikMasalar():
	os.chdir(directory + tarih)
	dirLst = os.listdir(".")
	dirLst.sort()
	cntr = 0
	for dosya in dirLst :
		if dosya[0] == "M" :
			cntr = cntr + 1

	if cntr == 0 :
		print "Acik masa yok!"
	else :
		print "Acik masalar:"
		for dosya in dirLst :
			if dosya[0] == "M" :
				print dosya

	return 0


def toplamHasilatayaz(masa_no, hesap):
	os.chdir(directory + tarih)
	f = open("Hasilat_Dokumu", 'a+')
	f.write("Masa" + str(masa_no) + " = " + str(hesap) + " TL")
	f.write("\n")
	f.close()

	f1 = open("toplam_hasilat", 'a+')
	hasilat = int(f1.read())
	f1.close()
	os.remove("toplam_hasilat")

	f2 = open("toplam_hasilat", 'a+')
	f2.write(str(int(hesap) + hasilat))
	f2.close()
	

def hasilatHesapla(masa_no):
	os.chdir(directory + tarih)
	f = open("Masa" + str(masa_no), 'r+')
	line_lst = f.readlines()
	f.close()
	length = len(line_lst)
	son_satir = line_lst[length-1]

	first_index = 0
	last_index = len(son_satir) - 4
	i = 0
	for harf in son_satir :
		i = i + 1
		if harf == "=" :
			first_index = i + 1

	toplam = ""
	while first_index <= last_index :
		toplam = toplam + son_satir[first_index]
		first_index = first_index + 1

	masa_hesap = int(toplam)
	toplamHasilatayaz(masa_no, masa_hesap)


def gunSonuHasilat():
	os.chdir(directory + tarih)
	f = open("toplam_hasilat", 'r+')
	print "Toplam Hasilat : %s TL" %f.read()
	f.close()

	return 0


def hasilatDokumu():
	os.chdir(directory + tarih)
	f = open("Hasilat_Dokumu", 'r+')
	hasilat_lst = f.readlines()
	f.close()
	print "Hasilat Dokumu:\n"
	for hasilat in hasilat_lst :
		print hasilat


def initDirs():
	util.createDir(directory)
	os.chdir(directory)
	util.createDir(tarih)
	os.chdir(tarih)
	if not os.path.exists(directory + tarih + "/" + "Hasilat_Dokumu") :
		f = open("Hasilat_Dokumu", 'a+')
		f.close()
	
	if not os.path.exists("toplam_hasilat") :
		f1 = open("toplam_hasilat", 'a+')
		f1.write("0")
		f1.close()


def main():
	while True:
		time.sleep(0.5)
		os.system("clear")
		if not os.path.exists(menuDosya):
			raw_input("Menu olusturmaniz gerekmektedir.\nDevam etmek icin bir tusa basiniz")
			fiyatGuncelle()




		print "\n1.Siparis Gir\n2.Masa Aktar\n3.Masa Hesap\n4.Acik Masalar\n5.Gun Sonu Hasilat\n6.Gun Sonu Hasilat Dokumu\n7.Menu Duzenle\n8.Cikis\n"
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
					print "line:426 Girdiginiz karakter bir sayi degil"
					return 0
			elif val == 4:
				acikMasalar()
				enter = raw_input("\nDevam etmek icin bir tusa basin")
			elif val == 5:
				gunSonuHasilat()
				enter = raw_input("\nDevam etmek icin bir tusa basin")
			elif val == 6:
				hasilatDokumu()
				enter = raw_input("Devam etmek icin bir tusa basin")
			elif val == 7:
				menuDuzenle()
			elif val == 8:
				break
			else :
				print "Gecersiz Secim!!!"
		except ValueError:
			print "line: 444 Girdiginiz karakter bir sayi degil!!!"


	return 0

if __name__ == "__main__":
    main()
