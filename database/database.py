#!/usr/bin/python

import os , sys
import time
import datetime
from time import strftime
import sqlite3


directory = "/home/ekent/projects/denemeler/python/database"

sys.path.append("/home/ekent/projects/denemeler/python")
import util

db_name = "db.sqlite"


def getFullDataFromDB() :

	print "\n"

	#kitapAdi = "UZMANLAR ICIN PHP"
	#yazarAdi = ("Mehmet Samli",)
	#fiyat = ""

	conn = sqlite3.connect("kitaplar.sqlite")
	cursor = conn.cursor()

	cursor.execute("SELECT * FROM kitaplar")
	rows = cursor.fetchall()

	conn.commit()
	conn.close()

	for row in rows:
		try:
			strkitap = row[0]
			stryazar = row[1]
			strfiyat = row[2]
			strline = strkitap
			for i in range(55 - len(strkitap)):
				strkitap = strkitap + " "

			for i in range(35 - len(stryazar)):
				stryazar = stryazar + " "

			strline = strkitap + stryazar + strfiyat
			print strline

		except UnicodeEncodeError:
			print "Turkce karakter sorunu"

	print "\n"

	return




def getDataKitapAdinaGore(kitapAdi):
	kitapAdi = kitapAdi.upper() #kitap isimleri db'de buyuk harfle kayitli

	conn = sqlite3.connect("kitaplar.sqlite")
	cursor = conn.cursor()

	#cursor.execute("SELECT * FROM kitaplar where KitapAdi='%s'" %kitapAdi)
	cursor.execute("SELECT * FROM kitaplar")
	rows = cursor.fetchall()

	conn.commit()
	conn.close()

	print " "
	match = 0
	for row in rows:
		try:
			strkitap = row[0]
			stryazar = row[1]
			strfiyat = row[2]
			strline = strkitap

			if not kitapAdi in strkitap:
				continue

			for i in range(55 - len(strkitap)):
				strkitap = strkitap + " "

			for i in range(35 - len(stryazar)):
				stryazar = stryazar + " "

			strline = strkitap + stryazar + strfiyat
			print strline + "\n"
			match = match+1

		except UnicodeEncodeError:
			print "Turkce karakter sorunu"

	if match == 0:
		print "Bu isimde kitap yok!\n"

	return




def getDataYazaraGore(yazarAdi):
	yazarAdi = yazarAdi.title() #yazar isimlerinin bas harfleri db'de buyuk harfle kayitli
	
	conn = sqlite3.connect("kitaplar.sqlite")
	cursor = conn.cursor()

	#cursor.execute("SELECT * FROM kitaplar where Yazar='%s'" %yazarAdi)
	cursor.execute("SELECT * FROM kitaplar")
	rows = cursor.fetchall()

	conn.commit()
	conn.close()

	print " "
	match = 0
	for row in rows:
		try:
			strkitap = row[0]
			stryazar = row[1]
			strfiyat = row[2]
			strline = strkitap

			if not yazarAdi in stryazar:
				continue

			for i in range(55 - len(strkitap)):
				strkitap = strkitap + " "

			for i in range(35 - len(stryazar)):
				stryazar = stryazar + " "

			strline = strkitap + stryazar + strfiyat
			print strline + "\n"
			match = match+1

		except UnicodeEncodeError:
			print "Turkce karakter sorunu"

	if match == 0:
		print "Bu isimde yazar yok!\n"

	return




def getDataFiyataGore(altLimit, ustLimit):
	conn = sqlite3.connect("kitaplar.sqlite")
	cursor = conn.cursor()

	cursor.execute("SELECT * FROM kitaplar")
	rows = cursor.fetchall()

	conn.commit()
	conn.close()

	print " "
	match = 0
	for row in rows:
		try:
			strkitap = row[0]
			stryazar = row[1]
			strfiyat = row[2]

			tamFiyat = strfiyat.split(",")[0]
			kusurat = strfiyat.split(",")[1]
			if not (int(altLimit) <= int(tamFiyat) and int(tamFiyat) <= int(ustLimit)):
				continue

			match = match+1
			strline = strkitap
			for i in range(55 - len(strkitap)):
				strkitap = strkitap + " "

			for i in range(35 - len(stryazar)):
				stryazar = stryazar + " "

			strline = strkitap + stryazar + strfiyat
			print strline + "\n"

		except UnicodeEncodeError:
			print "Turkce karakter sorunu"

	if match == 0:
		print "Secilen fiyat araliginda kitap bulunamadi!\n"

	return




def getDataFromDB() :
	while  True:
		choice = raw_input("\n  1.Butun Kitaplar\n  2.Kitap Adina Gore\n  3.Yazara Gore\n  4.Fiyata Gore\n  5.Cikis\n")
		if choice == "1":
			getFullDataFromDB();
			return
		elif choice == "2":
			kitapAdi = raw_input("Kitabin Adini Giriniz:")
			getDataKitapAdinaGore(kitapAdi)
			return
		elif choice == "3":
			yazarAdi = raw_input("Yazarin Adini Giriniz:")
			getDataYazaraGore(yazarAdi)
			return
		elif choice == "4":
			altLimit = raw_input("Alt Limiti Giriniz:")
			ustLimit = raw_input("Ust Limiti Giriniz:")
			getDataFiyataGore(altLimit, ustLimit)
			return
		elif choice == "5":
			return
		else:
			print "Gecersiz Secim\nTekrar Giriniz"


	return




def insertDB(infoLst) :
	conn = sqlite3.connect(db_name)
	curs = conn.cursor()

	curs.execute('''CREATE TABLE IF NOT EXISTS Personal_Information
						(name text, placeofbirth text, birthdate text, sex text)''')
	curs.execute("INSERT INTO Personal_Information VALUES ('%s', '%s', '%s', '%s')" %(infoLst[0], infoLst[1], infoLst[2], infoLst[3]))

	conn.commit()
	conn.close()




def getInformation() :
	infoLst = []
	cins = ""
	isim = ""
	ad = raw_input("\nAd:")
	soyad = raw_input("Soyad:")
	dogumyeri = raw_input("Dogum yeri:")
	dogumtarihi = raw_input("Dogum Tarihi(GG.AA.YYYY):")
	sex = raw_input("Cinsiyet(E/K):")
	if sex == "E" or sex == "e":
		cins = "Erkek"
	elif sex == "K" or sex == "k":
		cins = "Kiz"
	else:
		print "Gecersiz cinsiyet secimi!"
		return 0


	isim = str(ad) + " " + str(soyad)
	infoLst.append(isim)
	infoLst.append(dogumyeri)
	infoLst.append(dogumtarihi)
	infoLst.append(cins)

	print "\nAd Soyad:%s\nDogum Yeri:%s\nDogum Tarihi:%s\nCinsiyet:%s\n" %(isim, dogumyeri, dogumtarihi, cins)
	onay = raw_input("Onayliyor musunuz?(E/H):")
	if onay == "E" or onay == "e":
		print "Onaylandi"
		insertDB(infoLst)
	else:
		print "Onaylanmadi!"





def main():
	os.system("reset")
	choice = raw_input("1.Veri Gir\n2.Veri Cek\n")
	if choice == "2":
		getDataFromDB()
		return 0
	elif choice == "1":
		getInformation()
	else:
		print "Hatali secim!"


	return 0


if __name__ == "__main__":
    main()

