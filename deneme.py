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

libDir = os.path.join("C:/", "Users", "fmadran", "Desktop", "FADIL", "myProjects", "python")
directory = os.path.join(libDir, "siparis")
sys.path.append(libDir)
import util

tarih = util.getDate()


menuDosya = os.path.join(directory, "menu.txt")


def main():

        cwd = os.getcwd()
        prnt = os.path.dirname(cwd)
        print "cwd:",cwd
        print "prnt",prnt
                 
        #f=open(menuDosya,'r')
        #satirlar =f.read().split('\n') #Dosyadaki tum satirlari okuyoruz
        #f.close()

        #for menu in satirlar:
            #print menu


    #print "Number:", len(sys.argv)
    #print "List:", str(sys.argv)
    #print "arg1:", str(sys.argv[1])


        return 0



if __name__ == "__main__":
    main()

