#!/usr/bin/env python

import Pyro4
import sys
import os

@Pyro4.expose
#################################################################  Natalia Zdrowak
class Serv:
	def __init__(self, daemon):
        	self.daemon = daemon


	def wysylanie(self):
	 	name=raw_input('Nazwa programu do wyslania: ')
		name1=name+'.py'
		
		try:	
			with open(name1) as file:
        			pass
			p = open(name1)
			kod = p.read()
			p.close()
 
		except IOError as e:
			print name1 + ' - Plik nie istnieje'	
			kod='Blad'
		
			
		return kod


	def mess(self, msg):
		print('Klient {}'.format(msg))
	
		


def main(argv):
	karta=sys.argv[1]
	ip = os.popen('ip addr show '+karta).read().split("inet ")[1].split("/")[0] #pobiera ip // enp0s3 zamienic na eth0 lub odpowiadajacy karcie danego komutera
	
	if len(sys.argv) != 2:
		print 'Za duzo argumentow wejsciowych'
	else:
		daemon = Pyro4.Daemon(ip,port=9990)
   		serv = Serv(daemon)
    		uri = daemon.register(serv, objectId='Server')
    		print(uri)
    		daemon.requestLoop()
	
	

if __name__ == "__main__":
    main(sys.argv[1])
