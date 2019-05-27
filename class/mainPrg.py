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

#OgrenciAraclar icerisindeki tum siniflari kullanacagiz
from OgrenciAraclar import *

directory = "/home/ekent/projects/denemeler/python/class"

sys.path.append("/home/ekent/projects/denemeler/python")
import util

def main():

	ogrenciAraclar = OgrenciAraclar()
	ogrenciler = ogrenciAraclar.ogrencileriOku('ogrenciler.txt');
	for ogrenci in ogrenciler:
		print ogrenci.toString()
	
	return 0



if __name__ == "__main__":
    main()

