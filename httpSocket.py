#!/usr/bin/python

import os , sys
from time import strftime
import datetime
import time
import urllib
import re

sys.path.append("/home/ekent/projects/denemeler/python")
import util


host = "213.14.60.241"
port = 80
request = "GET " + "/KayseriAdsService/SmartStop?Id=2fb54e8b-7dea-4578-ae2f-b73677adc430" + " HTTP/1.0\r\n" + "\r\n\r\n"


def main():

	#if len(sys.argv) > 1 and str(sys.argv[1] == "1"):
	#	os.system("clear")

	print "Yukleniyor..."

	received = util.httpGet(host, port, request)
	if received == "-1" :
		os.system("clear")
		print "%s adresine baglanilamadi!\n" %host
		return 0
	
	#print "Received: {}".format(received)
	lst = received.split("\r\n\r\n")
	xmlStr = str(lst[1])
	os.system("clear")
	print "\nxml:\n%s\n" %xmlStr

	xmlFile = "file.xml"
	if os.path.exists(xmlFile):
		os.remove(xmlFile)

	file = open(xmlFile, 'a+')
	file.write(xmlStr)
	file.close()

	remainingTimeLst = util.readXml(xmlFile, "Vehicle", "TimeRemaining")
	if len(remainingTimeLst) == 0 :
		print "\nAlinan metin XML formatinda degil!\n"
		os.remove(xmlFile)
		return 0

	for timeRemaining in remainingTimeLst :
		print timeRemaining

	os.remove(xmlFile)


	return 0



if __name__ == "__main__":
    main()

