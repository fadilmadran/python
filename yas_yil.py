#!/usr/bin/python

import os , sys
#import datetime
from datetime import date

def function(birthday):
	lst_date = birthday.split("/")
	if len(lst_date) != 3 :
		return -1

	today = date.today()
	print "date:%s" %date(today.year, today.month, today.day)

	yil = today.year - int(lst_date[2])
	ay = today.month - int(lst_date[1])
	gun = today.day - int(lst_date[0])

	if not 0 <= int(lst_date[1]) <= 12 :
		print "Girdiginiz ay hatali!"
		return 0

	if not 0 < int(lst_date[0]) < 32 :
		print "Girdiginiz gun hatali!"
		return 0

	if int(lst_date[1]) == 2 :
		if int(lst_date[0]) > 29 :
			print "Girdiginiz gun hatali"
			return 0

	if yil < 0 :
		print "\nBu yalan dunyaya henuz gelmediniz :)\n"
		return 0
	elif (yil == 0) and (ay < 0) :
		print "\nBu yalan dunyaya henuz gelmediniz :)\n"
		return 0
	elif (yil == 0) and (ay == 0) and (gun < 0) :
		print "\nBu yalan dunyaya henuz gelmediniz :)\n"
		return 0

	if ay <= 0 :
		if yil != 0 :
			yil = yil - 1
			ay = ay + 12

	if gun < 0 :
		ay = ay - 1
		gun = gun + 30
		
	if yil > 0 :
		print "\nBu yalan dunyada %d yil %d ay %d gun gecirdiniz :)\n" %(yil, ay, gun)
	elif ay > 0 :
		print "\nBu yalan dunyada %d ay %d gun gecirdiniz :)\n" %(ay, gun)
	elif gun > 0 :
		print "\nBu yalan dunyada sadece %d gun gecirdiniz :)\n" %gun

	return 0
	

def main():
	os.system("clear")
	birthday = raw_input("\nDogum Tarihiniz(GG/AA/YYYY):")
	rslt = function(birthday)
	if rslt == -1:
		print "Hatali tarih formati girdiniz!"
		return 0

	return 0

if __name__ == "__main__":
    main()

