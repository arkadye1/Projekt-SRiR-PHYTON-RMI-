#!/usr/bin/env python

import Pyro4

@Pyro4.expose

class Witaj:
	def wysylanie(self):
		p = open('program.py')
		try:
			kod = p.read()
		finally:
			p.close()
			return kod



daemon = Pyro4.Daemon()

uri = daemon.register(Witaj)

ns= Pyro4.locateNS();

ns.register('obj',uri);

print(uri)


daemon.requestLoop();
