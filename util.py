#!/usr/bin/python

import os , sys
from datetime import datetime
import time
from time import strftime
import socket
from xml.dom import minidom
import urllib
import re
import smtplib


def createDir(path):
	if not os.path.exists(path):
		os.makedirs(path)

def getTime():
	hour=strftime("%H")
	minute=strftime("%M")
	str_time = str(hour) + str(minute)
	return str_time

def getFullTime():
	return strftime("%H:%M:%S")


def getDate():
	year=strftime("%Y")
	month=strftime("%m")
	day=strftime("%d")
	str_date = str(year) + str(month) + str(day)
	return str_date

def getFullDate():
	return strftime("%Y.%m.%d")


def timeDifference(beginTime):
	#strftime("%Y.%m.%d %H:%M:%S")
	year=int(strftime("%Y"))
	month=int(strftime("%m"))
	day=int(strftime("%d"))
	hour=int(strftime("%H"))
	minute=int(strftime("%M"))
	secs=int(strftime("%S"))

	timeDiff = str(year - int(beginTime[0])) + ":" + str(month - int(beginTime[1])) + ":" + str(day - int(beginTime[2])) + ":" \
			 + str(hour - int(beginTime[3])) + ":" + str(minute - int(beginTime[4])) + ":" + str(secs - int(beginTime[5]))

	return timeDiff

def getUnixtime(timeLst):
	#dt = datetime.datetime(int(timeLst[0]), int(timeLst[1]), int(timeLst[2]), int(timeLst[3]), int(timeLst[4]), int(timeLst[5]))
	dt = datetime(int(timeLst[0]), int(timeLst[1]), int(timeLst[2]), int(timeLst[3]), int(timeLst[4]), int(timeLst[5]))
	return time.mktime(dt.timetuple())


def parseDateTime(dt):
	tarih = dt.split(" ")[0]
	saat  = dt.split(" ")[1]

	year  = tarih.split(".")[0]
	month = tarih.split(".")[1]
	day   = tarih.split(".")[2]

	hour   = saat.split(":")[0]
	minute = saat.split(":")[1]
	secs   = saat.split(":")[2]

	fullTimeLst = []
	fullTimeLst.append(year)
	fullTimeLst.append(month)
	fullTimeLst.append(day)
	fullTimeLst.append(hour)
	fullTimeLst.append(minute)
	fullTimeLst.append(secs)

	return fullTimeLst


def httpGet(host, port, request):
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect((host, port))
		sock.sendall(request)
		received = sock.recv(8192)
	except:
		print "Socket acilamadi yada baglanilamadi!"
		sock.close()
		return "-1"
	finally:
		sock.close()

	return received


def readXml(xmlFile, tag, subTag):
	subTagLst = []

	try:
		xmldoc = minidom.parse(xmlFile)
		itemLst = xmldoc.getElementsByTagName(tag)
		for s in itemLst:
			subTagLst.append(s.attributes[subTag].value)
	except:
		return []

	return subTagLst
