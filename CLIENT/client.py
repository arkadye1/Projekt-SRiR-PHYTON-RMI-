#!/usr/bin/env python

import Pyro4
import subprocess


class Wynik:
	def odpowiedz(self):
		output = subprocess.check_output(['python','program1.py'])
		return output



def main():
#ns= Pyro4.locateNS()
#uri = ns.lookup('obj')

	wynik = Wynik()
 	uri = 'PYRO:Server@localhost:9990'
	#x=Pyro4.Proxy("PYRONAME:obj.witaj")
	remote = Pyro4.Proxy(uri)
	print 'Otrzymany kod programu: '
	odpow=remote.wysylanie("Otrzymano Program")
	print(format(odpow))

	

	p = open('program1.py', 'w')
	p.write(remote.wysylanie("Program zapisany"))
	p.close()

	
	while True:
		n = input('Wybierz (2. Raport, 3.Koniec): ')
		if n ==1:
			wyn1=wynik.odpowiedz()
			odpow1=remote.wysylanie('Wynik programu: {}'.format(wyn1))
		
			print 'WYNIK OTRZYMANEGO PROGRAMU: ', wyn1

		elif n == 2:
			with open('program1.py', 'r') as file1:
    				with open('program2.py', 'r') as file2:
        				same = set(file1).intersection(file2)
	
			same.discard('\n')

			with open('raport.txt', 'w') as file_out:
    				for line in same:
        				file_out.write(line)
	
			p = open('raport.txt')
			try:
				kod = p.read()
			finally:
				p.close()
	
			odpow2=remote.wysylanie('Raport porownawczy (powtarzajace sie linie kodu) \n{}'.format(kod))	
			print "Raport wyslany"
    		

		elif n == 3:
    			print "***KONIEC POLACZENIA***"
			odpow3=remote.wysylanie("***KONIEC POLACZENIA***")
			
   			remote._pyroRelease()
			remote.shutdown()

	
if __name__ == "__main__":
    main()
