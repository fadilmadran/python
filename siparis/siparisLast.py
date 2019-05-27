#!/usr/bin/python

import os , sys
import time
import sqlite3
import string

currentDir = os.getcwd()
libDir = os.path.dirname(currentDir)
directory = os.path.join(currentDir, "Siparisler")
sys.path.append(libDir)
import util

tarih = util.getDate()

menuDosya = os.path.join(libDir, "siparis", "Siparisler", tarih, "menu.sqlite")
siparisDosya = os.path.join(libDir, "siparis", "Siparisler", tarih, "siparis.sqlite")
siparisOdenen = os.path.join(libDir, "siparis", "Siparisler", tarih, "siparisOdenen.sqlite")
hasilatDosya = os.path.join(libDir, "siparis", "Siparisler", tarih, "hasilat.sqlite")



def menuOlustur():

	open(menuDosya, 'a+')
	conn = sqlite3.connect(menuDosya)
	cursor = conn.cursor()
	cursor.execute('''CREATE TABLE menu
		 (urun text, fiyat integer)''')

	while True:
		try:
			urunAdi = raw_input("Urun:")
			urunFiyati = raw_input("Fiyat:")
			cursor.execute("INSERT INTO menu VALUES ('%s', %d)" %(urunAdi, int(urunFiyati)))
			print("Urun menuye eklendi")
			continueAdding = raw_input("Yeni urun ekle E/H:")
			if continueAdding == "E" or continueAdding == "e":
				continue
			else:
				break
		except:
			print("%s urunu menuye eklenemedi" %urunAdi)

	conn.commit()
	conn.close()


def menuDosyasiniOku():
	if not os.path.exists(menuDosya):
		print("Menu bulunamadi!")
		return

	conn = sqlite3.connect(menuDosya)
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM menu")
	rows = cursor.fetchall()
	print("")
	for row in rows:
		print("%s: %d TL" % (row[0], int(row[1])))

	raw_input("\nDevam etmek icin bir tusa basiniz")


def fiyatGuncelle():
	if not os.path.exists(menuDosya):
		print("Menu bulunamadi!")
		return

	conn = sqlite3.connect(menuDosya)
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM menu")
	rows = cursor.fetchall()
	print("")
	for row in rows:
		try:
			yeniFiyat = raw_input("%s:" %row[0])
			if yeniFiyat.isdigit():
				conn.execute("UPDATE menu SET fiyat=%d WHERE urun='%s'" % (int(yeniFiyat), row[0]))
				print("%s urunun fiyati %d TL olarak guncellendi" %(row[0], int(yeniFiyat)))
			else:
				print("%s urunu guncellenmedi!" %row[0])
		except:
			print("%s urunu guncellenemedi!%s" %row[0])

	conn.commit()
	conn.close()


def urunEkle():
	if not os.path.exists(menuDosya):
		print("Menu bulunamadi!")
		return

	conn = sqlite3.connect(menuDosya)
	cursor = conn.cursor()

	while True:
		urunAdi = raw_input("Urun:")
		urunFiyati = raw_input("Fiyat:")
		cursor.execute("INSERT INTO menu VALUES ('%s', %d)" %(urunAdi, int(urunFiyati)))
		print("%s menuye eklendi" %urunAdi)
		continueAdding = raw_input("Yeni urun ekle E/H:")
		if continueAdding == "E" or continueAdding == "e":
			continue
		else:
			break

	conn.commit()
	conn.close()


def menuIslem():
	print("Menu Islem")
	print("  1.Mevcut Menu\n  2.Fiyat Guncelle\n  3.Urun Ekle")
	menuChoice = raw_input("Seciminiz:")
	try:
		if menuChoice == "1":
			menuDosyasiniOku()
		elif menuChoice == "2":
			fiyatGuncelle()
		elif menuChoice == "3":
			urunEkle()
		else:
			print("Gecersiz secim!")
	except ValueError:
		print("Girdiginiz karakter bir sayi degil!")


def siparisEkrani():
	conn = sqlite3.connect(menuDosya)
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM menu")
	rows = cursor.fetchall()
	conn.close()

	connSiparis = sqlite3.connect(siparisDosya)
	cursorSiparis = connSiparis.cursor()
	tutar = 0
	eskiSiparisler = []
	masaNo = raw_input("Masa No:")
	cursorSiparis.execute("SELECT name FROM sqlite_master WHERE type=\"table\"")
	tables = cursorSiparis.fetchall()
	for table in tables:
		if table[0] == "masa%s" %masaNo :
			eskiSiparisler = eskiSiparis(masaNo)
			break

	cursorSiparis.execute("CREATE TABLE IF NOT EXISTS masa%d(urun text, fiyat integer, miktar integer)" %int(masaNo))
	try:
		for row in rows:
			miktar = raw_input("%s:" % row[0])
			if miktar.isdigit() and len(eskiSiparisler) > 0:
				for eski in eskiSiparisler:
					if row[0] == eski[0]:
						adet = int(miktar) + int(eski[2])
						tutar = tutar + (adet * (int(row[1])))
						cursorSiparis.execute("UPDATE masa%d SET miktar=%d WHERE urun='%s'" %(
							int(masaNo), adet, row[0]))
					else:
						tutar = tutar + ((int(miktar)) * (int(row[1])))
						cursorSiparis.execute("INSERT INTO masa%d VALUES ('%s', %d, %d)" % (
							int(masaNo), row[0], int(row[1]), int(miktar)))
			elif miktar.isdigit():
				tutar = tutar + ((int(miktar)) * (int(row[1])))
				cursorSiparis.execute("INSERT INTO masa%d VALUES ('%s', %d, %d)" % (
						int(masaNo), row[0], int(row[1]), int(miktar)))

		siparisOnay = raw_input("Siparisi onayla E/H:")
		if siparisOnay == "E" or siparisOnay == "e":
			connSiparis.commit()
			print("Siparis onaylandi")
		else:
			connSiparis.rollback()
	except:
		print("Siparis girilemedi!")

	connSiparis.close()


def eskiSiparis(masaNo):
	connEski = sqlite3.connect(siparisDosya)
	cursorEski = connEski.cursor()
	cursorEski.execute("SELECT * FROM masa%s" %int(masaNo))
	siparisler = cursorEski.fetchall()
	connEski.close()
	return siparisler


def siparisYaz():
	siparisEkrani()


def siparisGir():
	siparisYaz()


def masaAktar():
	eskiMasa = raw_input("Eski masa numarasi:")
	while eskiMasa == "" or not eskiMasa.isdigit():
		eskiMasa = raw_input("Lutfen bir masa numarasi giriniz:")


	connTables = sqlite3.connect(siparisDosya)
	cursorTables = connTables.cursor()

	try:
		cursorTables.execute("SELECT * FROM masa%d" %int(eskiMasa))
	except:
		print("Masa%d bulunamadi" %int(eskiMasa))
		connTables.close()
		return

	yeniMasa = raw_input("Yeni masa numarasi:")
	while yeniMasa == "" or not yeniMasa.isdigit():
		yeniMasa = raw_input("Lutfen bir masa numarasi giriniz:")

	try:
		cursorTables.execute("SELECT * FROM masa%d" %int(yeniMasa))
		print("Masa%d kapatilmamis" %int(yeniMasa))
		connTables.close()
		return
	except:
		try:
			print("Masa aktariliyor...")
			cursorTables.execute("ALTER TABLE masa%d RENAME TO masa%d" %(int(eskiMasa), int(yeniMasa)))
			print("Masa%d, masa%d'ye aktarildi" %(int(eskiMasa), int(yeniMasa)))
		except:
			print("Bir sorun olustu! Lutfen acik masalari kontrol edip tekrar deneyin")



def hesabiOde(masa_no, odemeTuru):
	print("Hesabi Ode")


def hesapKapat(masaNo):
	print("Hesap Kapat")
	connHesap = sqlite3.connect(siparisDosya)
	cursorTables = connHesap.cursor()
	cursorTables.execute("SELECT * FROM masa%d" %int(masaNo))
	rows = cursorTables.fetchall()
	connHesap.close()

	connMenu = sqlite3.connect(menuDosya)
	cursorMenu = connMenu.cursor()
	cursorMenu.execute("SELECT * FROM menu")
	urunler = cursorMenu.fetchall()
	connMenu.close()

	tutar = 0
	for row in rows:
		print row
		for urun in urunler:
			if row[0] == urun[0]:
				tutar = tutar + ((int(row[2])) * (int(urun[1])))

	print("Tutar:%d" %int(tutar))
	strTime = util.getTime()
	print("Time:%s" %strTime)

	connOdenen = sqlite3.connect(siparisOdenen)
	cursorOdenen = connOdenen.cursor()
	cursorOdenen.execute("CREATE TABLE IF NOT EXISTS odenen(masaNo integer, fiyat integer, miktar integer)")



def acikMasalar():
	conn = sqlite3.connect(siparisDosya)
	cursor = conn.cursor()
	cursor.execute("SELECT name FROM sqlite_master WHERE type=\"table\"")
	rows = cursor.fetchall()
	conn.close()
	print("Acik Masalar:")
	for row in rows:
		print("  %s" %(row[0].title()))


def toplamHasilataYaz(masaNo, hesapTutari, odemeTuru):
	print("Toplam Hasilata Yaz")


def hasilatHesapla(masa_no, odemeTuru):
	print("Hasilat Hesapla")
	toplamHasilataYaz(masa_no, hesapTutari, odemeTuru)


def gunSonuHasilat():
	print("Gun Sonu Hasilat")


def hasilatDokumu():
	print("Hasilat Dokumu")


def initDirs():
	util.createDir(directory)
	os.chdir(directory)
	util.createDir(tarih)
	os.chdir(tarih)
	open(siparisDosya, 'a+')
	open(siparisOdenen, 'a+')
	open(hasilatDosya, 'a+')

	connOdenen = sqlite3.connect(siparisOdenen)
	cursorOdenen = connOdenen.cursor()
	cursorOdenen.execute("CREATE TABLE IF NOT EXISTS OdemeTipleri(odemeTipi integer, aciklama text)")
	cursorOdenen.execute("INSERT INTO OdemeTipleri VALUES (1, 'Nakit')")
	cursorOdenen.execute("INSERT INTO OdemeTipleri VALUES (2, 'Kredi Karti')")
	connOdenen.close()




def main():

	initDirs()
	if not os.path.exists(menuDosya):
		raw_input("Menu olusturmaniz gerekmektedir.\nDevam etmek icin bir tusa basiniz")
		menuOlustur()
	while True:
		#os.system("clear")
		print("\n" * 60)

		print("\n1.Siparis Gir\n2.Masa Aktar\n3.Masa Hesap\n4.Acik Masalar\n5.Gun Sonu Hasilat\n6.Gun Sonu Hasilat Dokumu\n7.Menu Islemleri\n8.Cikis\n")
		choice = raw_input("Seciminiz:")
		try:
			val = int(choice)
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
					enter = raw_input("Girdiginiz karakter bir sayi degil!\nDevam etmek icin bir tusa bisiniz")
					#return 0
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
			enter = raw_input("Bir sorun olustu!\nDevam etmek icin bir tusa basin")
			continue
			#print "line: 491 Girdiginiz karakter bir sayi degil!!!"

		time.sleep(1)


	return 0


if __name__ == "__main__":
	main()


#### NOTLAR ####
#initDirs ve hesapKapat fonksiyonlarini calistir
#masaAktar fonksiyonunu duzenle
