# author : @Syhrularv_
# -*- coding: utf-8 -*-

import os, sys, fileinput

N = '\033[0m'
D = '\033[90m'
W = '\033[1;37m'
B = '\033[1;34m'
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'

ask = G + '[' + W + '?' + G + '] '
sukses = G + '[' + W + '√' + G + '] '
eror = R + '[' + W + '!' + R + ']'
banner = '''{}___________________________________________________________________{}
 ____       ____.   ______   __        __         _____   __
 |  /      / _  |   |  ___/  | |/```\  | |/```\  / __  \  | |/```\.
 |  |     / /_| |   |  |_,   |   /`\|  |   /`\|  | | | |  |   /`\|
 |  |    /____  |{} @ {}|   _|   |  |      |  |      | | | |  |  |{}
 |  |__/|    |  |   |  |_/|  |  |      |  |      | |_| |  |  |
 |______|    /___\  |_____|  /___\     /___\     \_____/  /___\{}
___________________________________________________________________'''.format(G,R,Y,R,W,G)
banner2 = """{}	    ___________________ ★ ___________________
	    | {}Recode :{} KMB.ID {}| ★ |{} WA :{}088217145014{}|
	    |_________________| ★ |_________________|
	         		★
		      {}MENU TOOLS OBFUSCATE
    		{}<=============/\==============>
    		 || {}[{}01{}] {} Decrypt Bash      {}||
    		 || {}[{}02{}] {} Encrypt Bash      {}||
    		 || {}[{}00{}] {} Exit program      {}||
	    	<=============\/==============>
""".format(C,W,Y,C,W,Y,C,G,C,G,W,G,B,C,G,W,G,Y,C,G,W,G,R,C)
print banner
print banner2

#### Encrypt ####
def enkrip():
   try:
       sc = raw_input(ask + W + "NAMA BAHAN" + G + "> " + Y)
       f = open(sc,'r')
       filedata = f.read()
       f.close()

       newdata = filedata.replace("eval","echo")

       out = raw_input(ask + W + "NAMA HASIL" + G + " > " + Y)
       f = open(out,'w')
       f.write(newdata)
       f.close()

       os.system("touch tes.sh")
       os.system("bash " + out + " > tes.sh")
       os.remove(out)
       os.rename("tes.sh", out)
       print (sukses + "Done..")

   except KeyboardInterrupt:
       print (eror + " Stopped!")
   except IOError:
       print (eror + " File Not Found!")

#### Decypt ####
def dekrip():
   try:
       script = raw_input(ask + W + "NAMA BAHAN " + G + "> " + B)
       output = raw_input(ask + W + "NAMA HASIL" + G + "> " + B)
       os.system("bash-obfuscate " + script + " -o " + output )
       print (sukses + "Done..")
   except KeyboardInterrupt:
       print (eror + " Stopped!")
   except IOError:
       print (eror + " File Not Found!")

#### Close ####
def keluar():
    print (ask + R + """Thanks = by KMB•ID""" + eror)
    os.sys.exit

takok = raw_input(ask + W + " Pilih Angka" + G + " => ")

if takok == "1" or takok == "01":
   enkrip()
elif takok == "2" or takok == "02":
   dekrip()
elif takok == "0" or takok == "00":
   keluar()
else:
   print (eror + " DASAR TOLOL GK BISA BACA !!!")
