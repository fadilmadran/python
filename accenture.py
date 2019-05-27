#!/usr/bin/python
# coding=utf-8
import os , sys


def shifted_diff(first, second):
	if len(first) != len(second):
		return -1

	if first == second:
        	return 0

	n=1
	while(True):
		newStr = ""
		newStr = first[len(first)-1]
		newStr += first[0]
		for i in range(len(first)-2):
			newStr += first[i+1]
			
	
		print "newStr:", newStr
		first = newStr
		if(first == second):
			break
	
		n += 1
		if n > len(first):
			return -1
	
	return n


def main():
	
	first = "fatigue"
	second = "tiguefa"
	
	count = shifted_diff(first, second)
	print "shifted count:", count


    	return 0



if __name__ == "__main__":
    	main()
