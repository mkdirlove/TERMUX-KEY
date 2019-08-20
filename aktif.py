import os
import sys
from time import sleep

a ='\033[92m'
b ='\033[91m'
c ='\033[0m'

def printx(x):
        w = {'m':31,'h':32,'k':33,'b':34,'p':35,'c':36,'p':37}
        for i in w:
                x=x.replace('\r%s'%i,'\033[%s;1m'%w[i])
        x+='\033[0m'
        x=x.replace('\r0','\033[0m')
        print(x)

def info():
	os.system('clear')
	printx ('''
\rh                  ADD TERMUX KEYS
    (RIGHT, LEFT, PAGE UP, PAGE DOWN, HOME, END)

\rp________________________________________________________

\rh  Author  \rp: \rmDark-Link
\rh  Facebook\rp: \rmhttps://facebook.com/100026360573112
             \rp(\rmDark-Link Net ID\rp)
\rh  Github  \rp: \rmhttps://github.com/D4rk-L1nk/Termux-Key
\rh  E-Mail  \rp: \rmblackholecyber9@gmail.com
\rp________________________________________________________

\rk         Contact me if there is damage or error
              when running the program''')

def add():
	info()
	sleep(2.5)
	printx (' ')
	printx ('\rp    ........................................')
	printx ('\rh     [*] Processing...')
	printx ('\rp    ........................................')
	sleep(2.5)
	os.system('clear')
	info()
	printx (' ')
	printx ('\rp    ........................................')
	printx ('\rh     [*] Retrieve the default termux file')
	printx ('\rp    ........................................')
	sleep(2.5)
	os.system('clear')

	try:
	      os.mkdir('/data/data/com.termux/files/home/.termux')
	except:
	      pass

	key = "extra-keys = [['ESC','CTRL','ALT','PGUP','UP','PGDN','DOWN'],['TAB','/','-','HOME','LEFT','END','RIGHT']]"
	c = open('/data/data/com.termux/files/home/.termux/termux.properties','w') 
	c.write(key)
	c.close()
	info()
	printx (' ')
        printx ('\rp    ........................................')
	printx ('\rh     [!] Please waitt...')
	printx ('\rp    ........................................')
	sleep(4)
	os.system('termux-reload-settings')
	os.system('clear')
	info()
        printx (' ')
        printx ('\rp    ........................................')
        printx ('\rh     [*] Success ')
        sleep(1)
        printx ('\rh     [*] Additional buttons have been added')
        printx ('\rp    ........................................')
	printx (' ')
	printx (' ')
        sleep(2.5)

add()
