# Author Pei-Chen Tsai aka Hammer
# Ok, the line break position is impossible to 100% accurate currently, so just tune global parameter for your own purpose

import os, sys, re, codecs, io
import urllib
import urllib.request, urllib.error
import argparse
import logging
import platform
from os.path import expanduser
from pprint import pprint
from bs4 import BeautifulSoup,NavigableString

global DB
global args
global ARGUDB #arugment database
global tPage
global mProun

mProun = []
ARGUDB        = []
tPage         = ''
INSFOLDER = ''
bWindows = False

def strip_tags(html, invalid_tags):
    stripSoup = BeautifulSoup(html)

    for tag in stripSoup.findAll(True):
        if tag.name in invalid_tags:
            s = ""

            for c in tag.contents:
                if not isinstance(c, NavigableString):
                    c = strip_tags(unicode(c), invalid_tags)
                s += unicode(c)

            tag.replaceWith(s)
    return stripSoup

def repeatStr(string_to_expand, length):
	return (string_to_expand * ((length/len(string_to_expand))+1))[:length]

def htmlParser(tPage):
    resp = urllib.request.urlopen(url=tPage)
    if resp.code == 200 :
        data = resp.read()
        resp.close()
    elif resp.code == 404 :
        print("page do not exist")
        exit()
    else :
        print("can not open page")
        exit()

    soup = BeautifulSoup(data)

    print("beautifulSoup result")
    result = soup.findAll('span',{'class','fz-14'})
    result += soup.findAll('li',{'class':['lh-22 mh-22 ml-50 mt-12 mb-12','lh-22 mh-22 ml-50 mt-12 mb-12 last']});
    
    return result

#[]== maybe textwrapper, it's better than this hardcode

def prettyPrint(resultString):
    if bWindows :
        os.system('cls')
    else:
        os.system('clear')

    #for tag in ARGUDB:
    #    resultString = re.sub(r''+tag,'\n'+tag+'\n    ',resultString)
    print('search target:'+tPage)
    for line in resultString:
        print(line.get_text())

def loadArgumentDb():
	home = expanduser('~')
	if os.path.isfile(home+args.database) is True:
		f = codecs.open(home+args.database,encoding='UTF-8',mode='r')
		if f is not None:
			for line in f:
				if line != '\n' and line[0] != '#':
					line = line.rstrip('\n')
					global ARGUDB
					ARGUDB.append(line)
			f.close()
		else:
			DB.error('db file open fail')
	else :
		print('database doesn\'t existed')
	#print ARGUDB
	#raw_input()

def main():
   resultString = htmlParser(tPage)
   prettyPrint(resultString)

def setup_logging(level):
	global DB
	DB = logging.getLogger('edict') #replace
	DB.setLevel(level)
	handler = logging.StreamHandler(sys.stdout)
	handler.setFormatter(logging.Formatter('%(module)s %(levelname)s %(funcName)s| %(message)s'))
	DB.addHandler(handler)

def verify():
	global tPage
	global args
	parser = argparse.ArgumentParser(description='A English Dictionary Utility') #replace
	parser.add_argument('-v', '--verbose', dest='verbose', action = 'store_true', default=False, help='Verbose mode')
	parser.add_argument('query', nargs='*', default=None)
	parser.add_argument('-d', '--database', dest='database', action = 'store', default='/.hmDict/edict.db') #replace
	args = parser.parse_args()
	tPage = ' '.join(args.query)
	log_level = logging.INFO
	if args.verbose:
		log_level = logging.DEBUG
	if not tPage:
		parser.print_help()

if __name__ == '__main__':
	verify()
	loadArgumentDb()
	main()
