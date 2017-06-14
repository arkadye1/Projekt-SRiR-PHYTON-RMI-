#!/usr/bin/env python

import Pyro4
import subprocess
import sys
import os


class Wynik:

################################################################################# Arkadiusz Wojcik
	
	def zadania(self,remote):
	    wynik = Wynik()
	    twplik = 0
	    myip = os.popen('ip addr show enp0s3').read().split("inet ")[1].split("/")[0]	#zamiana enp0s3 na eth0

	    while True:
		n = input('Wybierz (1.Pobierz program, 2. Wykonaj program, 3. Raport, 4.Koniec): ')
		if n == 1:
			print 'Oczekiwanie na program: '
			odpow=remote.wysylanie()
			if odpow != 'Blad':
				print 'Otrzymany kod programu: '
				remote.mess(myip+": Otrzymano Program")
				print(format(odpow))
			
		   
				twplik=raw_input('Zapisz jako: ')
				p = open(twplik+'.py', 'w')
				p.write(odpow)
				remote.mess(myip+": Zapisano Program ")
				p.close()
				print "Zapisano poprawinie"
			else:
				print 'Wystapil blad. Sprobuj pobrac program jeszcze raz'

################################################################################# Michal Wrzesien

		if n == 2:
			if twplik!=0:
				wyn1 = subprocess.check_output(['python',twplik+'.py'])
				remote.mess(myip+': Wynik programu:\n{}'.format(wyn1))
				print 'WYNIK OTRZYMANEGO PROGRAMU:\n', wyn1
			else:
				print 'Nie mozna wykonac. Pobierz program!'

################################################################################# Jakub Zub

		elif n == 3:
			name1 = raw_input('Program 1: ')
			name2 = raw_input('Program 2: ')
			try:
				with open(name1+'.py', 'r') as file1:
					pass
    					with open(name2+'.py', 'r') as file2:
						pass
        					same = set(file1).intersection(file2)
	
						same.discard('\n')

				with open('raport.txt', 'w') as file_out:
    					for line in same:
        					file_out.write(line)

	
				p = open('raport.txt')
				try:
					rap = p.read()
				finally:
					p.close()
	
				remote.mess(myip+': Raport porownawczy (powtarzajace sie linie kodu) \n{}'.format(rap))
				print "Powtarzajace sie linie kodu:"
				print (format(rap))
				
				print "Raport wyslany!"
			except IOError as e:
				print  'Blad. Nieprawidlowa nazwa ktoregos z plikow'	
				
################################################################################# Michal Wrzesien
    		

		elif n == 4:
    			print "***KONIEC POLACZENIA***"
			remote.mess("***KONIEC POLACZENIA*** - "+myip)
			
   			break	
			

################################################################################# Arkadiusz Wojcik

def main(argv):
#ns= Pyro4.locateNS()
#uri = ns.lookup('obj')
	ipv4 = sys.argv[1]
	card = sys.argv[2]
	
	myip = os.popen('ip addr show '+card).read().split("inet ")[1].split("/")[0]	#zamiana enp0s3 na eth0

	if len(sys.argv) != 3:
		print 'Za duzo argumentow wejsciowych'
		
	else:
		wynik = Wynik()
 		uri = 'PYRO:Server@'+ipv4+':9990'
		#x=Pyro4.Proxy("PYRONAME:obj.witaj")
		remote = Pyro4.Proxy(uri)
		
		remote.mess("***NAWIAZANO POLACZENIE*** " + myip)
		print '***NAWIAZANO POLACZENIE***'
		wynik.zadania(remote)

	
	
if __name__ == "__main__":
    main(sys.argv[2])
