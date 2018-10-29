#-------------------------------------------------------------------------------IMPORTS-------------------------------------------------------------------------
import hashlib
import sys
import time
import os
from hashlib import *
#--------------------------------------------------------------------------------Color--------------------------------------------------------------------------
red='\033[1;31m'
green='\033[1;32m'
orange='\033[1;33m'
blue='\033[1;34m'
gray='\033[1;37m'
#-------------------------------------------------------------------------------Slow text-----------------------------------------------------------------------
def slow(M):
	for c in M+'\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./100)

os.system('clear')
print(green+'''                         
                 ***111****1R888L
            L41**          488884
          **               L8888881
        *1             *LH888888888*
      **               1L44LLLL48L
                  *11111111***11*
                 *R8888888888841
                 L88888888888888
                 148888L11*111H81'''
, red+
'''Telegram: HACKEER1'''
,green+
'''\n                  *888L   1L44L81'''
,red+
'''Facebook: KING.HACKING.SY'''
,green+ 
'''\n                   *48HL4L11LH888'''
,red+
'''Instgram: KING1HACKING'''
,green+
'''\n                     88R   *1LLR1'''
,red+
'''Whatsapp: 00963937376654'''
,green+
'''\n                     888888888881
                     88888888888*
                     444888R1148
                       *111 11RL
                    *1 **1LR8R4
                     *1888888L
                      18888H*
                      *88H*
                      1L*''')
slow (green+'         The script By:'+red+'KiNg-HaCkInG')
slow(green+'           Virtual Justice System')
print()
slow(red+'{1}-'+green+'Making Hash')
print()
slow(red+'{2}-'+green+'Type Hash')
print()
slow(red+'{3}-'+green+'Cracking Hash')
print()
slow(red+'{4}-'+green+'Exit')
print()
def kinga():
	number=str(input(green+'Enter the Number: '+blue))
	#---------------------------------------------------------------------------------Make Hash------------------------------------------------------------------
	if number == str('1') :
		print()
		print()
		os.system('clear')
		print(green+'''                         
                 ***111****1R888L
            L41**          488884
          **               L8888881
        *1             *LH888888888*
      **               1L44LLLL48L
                  *11111111***11*
                 *R8888888888841
                 L88888888888888
                 148888L11*111H81'''
, red+
'''Telegram: HACKEER1'''
,green+
'''\n                  *888L   1L44L81'''
,red+
'''Facebook: KING.HACKING.SY'''
,green+ 
'''\n                   *48HL4L11LH888'''
,red+
'''Instgram: KING1HACKING'''
,green+
'''\n                     88R   *1LLR1'''
,red+
'''Whatsapp: 00963937376654'''
,green+
'''\n                     888888888881
                     88888888888*
                     444888R1148
                       *111 11RL
                    *1 **1LR8R4
                     *1888888L
                      18888H*
                      *88H*
                      1L*''')
		print()
	#---------------class hash-------------------
		class hashtext:
			def logo(self,text,hash_type):
				text = text.encode("utf-8")
				hash_hash = hashlib.new(hash_type)
				hash_hash.update(text)
				return hash_hash.hexdigest()
	#----------------read Text-------------------		
		slow (green+'         The script By:'+red+'KiNg-HaCkInG')
		slow(green+'           Virtual Justice System')
		print()
		text = str (input(green+'Enter The Text Now : '+blue))
	#----------------read Hash-------------------
		hashtextt = str (input(green+'Enter Type The Hash: '+blue))
	#----------------while text------------------
		while text == '':
			slow(red+'            Erorr')
			slow(red+'Please Enter Any text first ^_^')
			text = str (input(green+'Enter the Text Now : '+blue))
	#----------------while hash------------------
		while hashtextt == '':
			slow(red+'              Erorr')
			slow(red+'Please Enter Any Type Hash Now ^_^')
			hashtextt = str (input(green+'Enter Type The Hash: '+blue))
	#-----------print Hash and type hash----------
		King = hashtext()
		print()
		print()							
		print(green+'HASH'+green+' ==='+blue+'{'+red+(hashtextt)+blue+'}'+green+'===>'+orange+'{',King.logo(text,hashtextt),'}')
		k=input(green+'            Prease any Kay')
		os.system('python3 MK_hash.py')

	#------------------------------------------------------------------------------Type Hash--------------------------------------------------------------------
	elif number == str('2') :
		os.system('clear')
		print(green+'''                         
                 ***111****1R888L
            L41**          488884
          **               L8888881
        *1             *LH888888888*
      **               1L44LLLL48L
                  *11111111***11*
                 *R8888888888841
                 L88888888888888
                 148888L11*111H81'''
, red+
'''Telegram: HACKEER1'''
,green+
'''\n                  *888L   1L44L81'''
,red+
'''Facebook: KING.HACKING.SY'''
,green+ 
'''\n                   *48HL4L11LH888'''
,red+
'''Instgram: KING1HACKING'''
,green+
'''\n                     88R   *1LLR1'''
,red+
'''Whatsapp: 00963937376654'''
,green+
'''\n                     888888888881
                     88888888888*
                     444888R1148
                       *111 11RL
                    *1 **1LR8R4
                     *1888888L
                      18888H*
                      *88H*
                      1L*''')
		print()
		king=str(input(green+'Enter the Hash: '+blue))
		if len(king) == 32 :
			print()
			print (green+'Type Hash'+blue+' ==================>'+red+' {'+green+'MD4'+red+' or'+green+' MD5'+red+'}')
		elif len(king) == 64 :
			print()
			print (green+'Type Hash'+blue+' ==================>'+red+' {'+green+'SHA256'+red+'}')
		elif len(king) == 128 :
			print()
			print (green+'Type Hash'+blue+' ==================>'+red+' {'+green+'SHA512'+red+' or'+green+' Whirlpool'+red+'}')
		elif len(king) == 56 :
			print()
			print (green+'Type Hash'+blue+' ==================>'+red+' {'+green+'SHA224'+red+'}')
		elif len(king) == 40 :
			print()
			print (green+'Type Hash'+blue+' ==================>'+red+' {'+green+'SHA1'+red+' or'+green+' DSA'+red+' or' +green+' RIPEMD160'+red+'}')
		else:
			slow(red+'Type Hash does not exist in My List')
			o=str(input(green+'             Enter any kay'))
			os.system('python3 MK_hash.py')

#----------------------------------------------------------------------------------------face hash-----------------------------------------------------------------------------------------
	
	elif number == str('3') :
		def king1():
			os.system('clear')
			print(green+'''                         
                 ***111****1R888L
            L41**          488884
          **               L8888881
        *1             *LH888888888*
      **               1L44LLLL48L
                  *11111111***11*
                 *R8888888888841
                 L88888888888888
                 148888L11*111H81'''
, red+
'''Telegram: HACKEER1'''
,green+
'''\n                  *888L   1L44L81'''
,red+
'''Facebook: KING.HACKING.SY'''
,green+ 
'''\n                   *48HL4L11LH888'''
,red+
'''Instgram: KING1HACKING'''
,green+
'''\n                     88R   *1LLR1'''
,red+
'''Whatsapp: 00963937376654'''
,green+
'''\n                     888888888881
                     88888888888*
                     444888R1148
                       *111 11RL
                    *1 **1LR8R4
                     *1888888L
                      18888H*
                      *88H*
                      1L*''')
			print()
			slow(orange+'          Enter Number Type The Hash')
			slow(red+'{1}-'+green+'Md5')
			print()
			slow(red+'{2}-'+green+'sha1')
			print()
			slow(red+'{3}-'+green+'sha256')
			print()
			slow(red+'{4}-'+green+'sha512')
			print()
			slow(red+'{5}-'+green+'sha224')
			print()
			slow(red+'{9}-'+green+'back')
			print()
			ch=str(input('Enter the Number: '+blue))


			if ch == str('1'):
				print()
				hash=input(green+'Enter The Hash Now: '+blue)
				file=input(green+'Enter The Wordlist: '+blue)
				with open(file,mode='r') as ms:
					for line in ms:
						line=line.strip()
						if md5(line.encode()).hexdigest()==hash:
							print()
							print(green+'{+} The Passowrd is: ',line)
							exit()
						elif md5(line.encode()).hexdigest()!=hash:
							print(gray+md5(line.encode()).hexdigest(),'==================>','Not Found!!!',line)

			elif ch == str('2'):
				print()
				hash=input(green+'Enter The Hash Now: '+blue)
				file=input(green+'Enter The Wordlist: '+blue)
				with open(file,mode='r') as ms:
					for line in ms:
						line=line.strip()
						if sha1(line.encode()).hexdigest()==hash:
							print()
							print(green+'{+} The Passowrd is: ',line)
							exit()
						elif sha1(line.encode()).hexdigest()!=hash:
							print(gray+sha1(line.encode()).hexdigest(),'==================>','Not Found!!!')
			elif ch == str('3'):
				print()
				hash=input(green+'Enter The Hash Now: '+blue)
				file=input(green+'Enter The Wordlist: '+blue)
				with open(file,mode='r') as ms:
					for line in ms:
						line=line.strip()
						if sha256(line.encode()).hexdigest()==hash:
							print()
							print(green+'{+} The Passowrd is: ',line)
							exit()
						elif sha256(line.encode()).hexdigest()!=hash:
							print(gray+sha256(line.encode()).hexdigest(),'==================>','Not Found!!!')
			elif ch == str('4'):
				print()
				hash=input(green+'Enter The Hash Now: '+blue)
				file=input(green+'Enter The Wordlist: '+blue)
				with open(file,mode='r') as ms:
					for line in ms:
						line=line.strip()
						if sha512(line.encode()).hexdigest()==hash:
							print()
							print(green+'{+} The Passowrd is: ',line)
							exit()
						elif sha512(line.encode()).hexdigest()!=hash:
							print(gray+sha512(line.encode()).hexdigest(),'==================>','Not Found!!!')
			elif ch == str('5'):
				print()
				hash=input(green+'Enter The Hash Now: '+blue)
				file=input(green+'Enter The Wordlist: '+blue)
				with open(file,mode='r') as ms:
					for line in ms:
						line=line.strip()
						if sha224(line.encode()).hexdigest()==hash:
							print()
							print(green+'{+} The Passowrd is: ',line)
							exit()
						elif sha224(line.encode()).hexdigest()!=hash:
							print(gray+sha224(line.encode()).hexdigest(),'==================>','Not Found!!!')
			elif ch == str('9'):
				os.system('clear')
				os.system('python3 MK_hash.py')
			else:
				slow(red+'              ERROR')
				slow(red+'           Enter {1..5}')
				king1()
		king1()
	
	
	#------------------------------------------------------------------------------Exit--------------------------------------------------------------------------
	elif number == str('4') or number == str('exit') :
		print()
		slow(red+'                            Good luck')
		exit()
	#------------------------------------------------------------------------------else--------------------------------------------------------------------------
	else:
		print (red+'Enter {1} or {2} or {3}')
		kinga()
		


kinga()
