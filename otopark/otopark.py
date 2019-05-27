#!/usr/bin/python

import os , sys
from time import strftime
import datetime
import time

directory = "/home/ekent/projects/denemeler/python/Otopark/"
sys.path.append("/home/ekent/projects/denemeler/python")
import util

tarih = util.getDate()

tarife0 = 0
tarife1 = 7200
tarife2 = 18000
tarife3 = 432000

parkUcreti1 = 5
parkUcreti2 = 9
parkUcreti3 = 15
parkUcreti4 = 20


def otoparkGiris():
	plaka = raw_input("Plaka:")

	if os.path.exists(directory + str(tarih) + "/" + str(plaka)):
		print "Bu arac otoparktan cikis yapmamis!"
		return 0
	else:
		os.chdir(directory + str(tarih))
		file = open(plaka, 'a+')
		file.write("Giris: " + str(util.getFullDate()) + " " + str(util.getFullTime()) + "\n")
		file.close()


def toplamHasilat():
	os.chdir(directory + tarih)
	file = open("toplam_hasilat", 'a+')
	toplamHasilat = file.read()
	file.close()
	print "Toplam Hasilat %s TL\n" %toplamHasilat

def hasilatDokumu():
	os.chdir(directory + tarih)
	file = open("Hasilat_Dokumu", 'a+')
	hasilatLst = file.readlines()
	print "Hasilat Dokumu:\n"
	for hasilat in hasilatLst :
		print hasilat


def tutarHesapla(girisUnixtime, cikisUnixtime):
	gecenSure = int(cikisUnixtime) - int(girisUnixtime)
	tutar = 0
	if tarife0 < gecenSure <= tarife1 :
		tutar = parkUcreti1
	elif tarife1 < gecenSure <=tarife2 :
		tutar = parkUcreti2
	elif tarife2 < gecenSure <= tarife3 :
		tutar = parkUcreti3
	elif gecenSure > tarife3 :
		tutar = parkUcreti4
	else:
		tutar = 0

	return tutar


def hasilatDosyalarinaYaz(plaka, tutar):
	os.chdir(directory + tarih)
	file = open(plaka, 'a+')
	content = file.read()
	file.close()
	dataLst = content.split("\n")
	dataStr = plaka
	for data in dataLst :
		dataStr = dataStr + " , " + str(data)

	fHasilatDokumu = open("Hasilat_Dokumu", 'a+')
	fHasilatDokumu.write(dataStr + "\n")
	fHasilatDokumu.close()

	fToplamHasilat = open("toplam_hasilat", 'a+')
	hasilat = int(fToplamHasilat.read())
	fToplamHasilat.close()
	os.remove("toplam_hasilat")
	fYeniToplam = open("toplam_hasilat", 'a+')
	fYeniToplam.write(str(hasilat + int(tutar)))
	fYeniToplam.close()




def otoparkCikis():
	plaka = raw_input("Plaka:")
	if not os.path.exists(directory + str(tarih) + "/" + str(plaka)):
		print "Bu plaka giris yapmamis!"
		return 0
	
	os.chdir(directory + str(tarih))
	file = open(plaka, 'a+')
	content = file.readlines()[0] #content: Giris: 2017.02.10 10:53:46
	file.close()

	girisTarihi = content.split(" ")[1]
	girisSaati  = content.split(" ")[2]
	girisTimeLst = []
	girisTimeLst = util.parseDateTime(girisTarihi + " " + girisSaati)
	girisUnixtime = util.getUnixtime(girisTimeLst)

	cikisTarihi = strftime("%Y.%m.%d %H:%M:%S")
	cikisTimeLst = util.parseDateTime(cikisTarihi)
	cikisUnixtime = util.getUnixtime(cikisTimeLst)

	tutar = tutarHesapla(girisUnixtime, cikisUnixtime)
	print "Tutar ",int(tutar), "TL"
	onay = raw_input("Aracin cikisini yap: e/h : ")
	if onay == "h" :
		print "Cikis yapilmadi!"
	elif onay == "e" or onay == "E" :
		os.chdir(directory + tarih)
		f = open(plaka, 'a+')
		f.write("Cikis: " + str(cikisTarihi) + "\n")
		f.write("Tutar: " + str(tutar) + " TL" "\n")
		f.close()
		hasilatDosyalarinaYaz(plaka, tutar)
		os.rename(plaka, "Odendi_" + str(plaka))
		print "Cikis yapildi"
	else:
		"Gecersiz secim!"

	return 0


def icerdekiAraclar():
	os.chdir(directory + tarih)
	aracLst = []
	dosyaLst = os.listdir(".")
	counter = 0
	for dosya in dosyaLst :
		if not (dosya == "toplam_hasilat" or dosya == "Hasilat_Dokumu" or dosya[:7] == "Odendi_"):
			counter = counter + 1
			aracLst.append(dosya)

	if counter == 0 :
		print "Otoparkta arac yok!"
		return 0

	print "Otoparkta %d adet arac var" %counter
	print "Icerdeki araclar:\n"
	for arac in aracLst :
		print arac

	print "\n"


def initDirs():
	util.createDir(directory)
	os.chdir(directory)
	util.createDir(tarih)
	os.chdir(tarih)
	if not os.path.exists(directory + tarih + "/" + "Hasilat_Dokumu"):
		f = open("Hasilat_Dokumu", 'a+')
		f.close()

	if not os.path.exists(directory + tarih + "/" + "toplam_hasilat"):
		f1 = open("toplam_hasilat", 'a+')
		f1.write("0")
		f1.close()

def main():

	while True:
		time.sleep(0.5)
		os.system("clear")
		print "1.Arac Giris\n2.Arac Cikis\n3.Icerideki Araclar\n4.Toplam Hasilat\n5.Hasilat Dokumu\n6.Cikis\n"
		choice = raw_input("Seciminiz:")
		try:
			val = int(choice)
			initDirs()
			if val == 1 :
				otoparkGiris()
			elif val == 2 :
				otoparkCikis()
			elif val == 3 :
				icerdekiAraclar()
				enter = raw_input("Devam etmek icin bir tusa basin")
			elif val == 4 :
				toplamHasilat()
				enter = raw_input("Devam etmek icin bir tusa basin")
			elif val == 5 :
				hasilatDokumu()
				enter = raw_input("Devam etmek icin bir tusa basin")
			elif val == 6 :
				break
			else :
				print "Gecersiz Secim!"
		except ValueError:
			print "line 201:Girdiginiz karakter sayi degil!"



	return 0



if __name__ == "__main__":
    main()

