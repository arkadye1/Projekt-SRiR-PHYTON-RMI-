#!/usr/bin/env python

import Pyro4

@Pyro4.expose

class Serv:
	def __init__(self, daemon):
        	self.daemon = daemon

	def wysylanie(self,msg):
		
		p = open('program.py')
		try:
			kod = p.read()
		finally:
			p.close()
		print('Klient: {}'.format(msg))
        	
		return kod
	
	
	#def polaczenie(self):
 		
		#daemon = Pyro4.Daemon()
		#ns= Pyro4.locateNS();
		#uri = daemon.register(Witaj)
		#ns.register("obj.witaj",uri)
		#print(uri)
		#daemon.requestLoop()

	#def odp(self,od):
		#print('client said {}'.format(od))
        	#return 'hola'
	
		


def main():
	
	daemon = Pyro4.Daemon(port=9990)
   	serv = Serv(daemon)
    	uri = daemon.register(serv, objectId='Server')
    	print(uri)
    	daemon.requestLoop()
	
	

if __name__ == "__main__":
    main()
