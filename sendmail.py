#!/usr/bin/python
# coding=utf-8
import os , sys
#from datetime import datetime
import time
import datetime
from time import strftime
import urllib
import re
import smtplib
import email.utils
from email.mime.text import MIMEText

directory = "/home/ekent/projects/denemeler/python"

sys.path.append("/home/ekent/projects/denemeler/python")
import util

def sendMultipleMail():
	
	mail_adresleri = ["fadil_madran@hotmail.com", "bugseerdogan@gmail.com", "fadil.madran@aktifbank.com.tr"] #email adreslerini liste halinde yaziyoruz
	
	kullanici = "fadilmadran@gmail.com" #smtp baglanti sirasinda oturum acmak icin kullanilacak email ve parolasini ayarlıyoruz
	sifre = "**********"
	gonderen_ismi = "Fadil Madran" #giden maillerde adimiz yazsin demi ya
	
	msg = MIMEText('Bu bir test mesajidir') #mesaj icerigini olusturuyoruz
	msg.set_unixfrom('author')
	
	msg['Subject'] = "Python Mail Deneme" #email konusu
	nmsg['From'] = email.utils.formataddr((gonderen_ismi, kullanici)) #kendi email adresimizi optimize ediyoruz
	
	sunucu = smtplib.SMTP("smtp.gmail.com:587") #sunucuya baglaniyoruz

	try:
	  
	  if sunucu.has_extn('STARTTLS'): #sunucu tls ise bunu yapsin
	    sunucu.starttls()
	   
	  server.login(kullanici, sifre)#giris yapiyoruz
	  
	  for mail_adres in mail_adresleri: #elimizde ki email listesini donguye sokuyoruz
	    
	    msg['To'] = email.utils.formataddr(("", mail_adres)) #gonderilecek email adresini optimize ediyoruz
	    gndr = sunucu.sendmail(kullanici, [mail_adres], msg.as_string()) #gonderiyoruz
	    print "Gonderildi : " + mail_adres
	    msg['To'] = "" #temizliyoruz bunu yapmasaniz da olur
	except:
	  print "Hata"
	finally:
	  sunucu.quit() #basarili biterse oturumu sondandiriyoruz



def sendMail():
	#### NOT: Kodumuzun calismasi icin Google daha az guvenli uygulamalara izin verin.

	kullanici = "fadilmadran@gmail.com"
	kullaniciSifresi = "**********" #sifreyi gir

	alici = "gonderilen@mail.com" # aliciyi gir
	konu = "Test"
	mesaj = "Deneme"

	email_text = """
	From: {}
	To: {}
	Subject: {}
	{}
	""" .format(kullanici,alici, konu, msj)

	try:
	    server = smtplib.SMTP('smtp.gmail.com:587')   #servere bağlanmak için gerekli host ve portu belirttik
	    server.starttls() #serveri TLS(bütün bağlantı şifreli olucak bilgiler korunucak) bağlantısı ile başlattık
	    server.login(kullanici, kullaniciSifresi)   # Gmail SMTP server'ına giriş yaptık
	    server.sendmail(kullanici, alici, email_text) # Mail'imizi gönderdik 
	    server.close()     # SMTP serverimizi kapattık
	    
	    print ('email gönderildi')
    
	except:
	    print("bir hata oluştu")


def main():

	return 0



if __name__ == "__main__":
    main()

