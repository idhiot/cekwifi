#!/usr/bin/env python
import os,sys,time

def menu ():
    print ("1.Cek password wifi")
    pilih = input ("Pilih nomor : ")
    if pilih == "1":
       os.system ("pkg install termux-tools")
       os.system ("su")

menu ()