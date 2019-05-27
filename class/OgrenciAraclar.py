#!/usr/bin/python
# coding=utf-8
import os , sys
#from datetime import datetime
import time
import datetime
from time import strftime
import sqlite3
import urllib
import re
import smtplib

directory = "/home/ekent/projects/denemeler/python/class"

from Ogrenci import *

class OgrenciAraclar:
    def ogrencileriOku(self,dosyaAdi):
        f=open(dosyaAdi,'r')
        satirlar =f.readlines() #Dosyadaki tum satirlari okuyoruz
        f.close()
        ogrenciler = []
        for ogrenciBilgisi in satirlar:
            #Dosyadan okudugumuz her satir icin Satirdaki ogrenci bilgisinden ogrenci nesnesini olusturup listemize ekliyoruz
            ogrenciler.append(self.__ogrenciUret(ogrenciBilgisi))
        
        return ogrenciler

    def __ogrenciUret(self,ogrenciBilgisi):
        ogrenciBilgisi = ogrenciBilgisi.replace('\n',' ').strip() #satir sonu karakterini yokediyoruz ve bosluklari kaldiriyoruz
        tokenler = ogrenciBilgisi.split('\t') #Ogrenci bilgisi stringini saha parcalarina ayiriyoruz
        return Ogrenci(tokenler[0],tokenler[1],tokenler[2],tokenler[3])

