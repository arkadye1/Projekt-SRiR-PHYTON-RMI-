#!/usr/bin/env python

import Pyro4
import subprocess



ns= Pyro4.locateNS()
uri = ns.lookup('obj')

x=Pyro4.Proxy(uri)
print 'Otrzymany kod programu: '
print (x.wysylanie())

p = open('program1.py', 'w')
p.write(x.wysylanie())
p.close()

output = subprocess.check_output(['python','program1.py'])

print 'WYNIK OTRZYMANEGO PROGRAMU: ', output

class Odp:
	def odpowiedz(self):
		return output


