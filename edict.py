# Author Pei-Chen Tsai

import os, sys, re, codecs, io
import urllib
import urllib.request, urllib.error
import argparse
import logging
import platform
import sqlite3
import openai
from HMTXCLR import clrTx
from os.path import expanduser
from pprint import pprint
from bs4 import BeautifulSoup,NavigableString

global DB
global args
global ARGUDB
global tPage
global mProun
global wordDb
global cursor
global ScreenI
global parser
global gOpenAIKEY

mProun = []
ARGUDB = []
ScreenI = []
tPage = 'https://tw.dictionary.search.yahoo.com/search?p='
INSFOLDER = ''
bWindows = False
gOpenAIKEY=''

def strip_tags(html, invalid_tags):
    stripSoup = BeautifulSoup(html)

    for tag in stripSoup.findAll(True):
        if tag.name in invalid_tags:
            s = ""

            for c in tag.contents:
                if not isinstance(c, NavigableString):
                    c = strip_tags(str(c,'utf8'), invalid_tags)
                s += str(c,'utf8')

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

def loadOpenAIKey():
    global gOpenAIKEY                    
    home = expanduser('~')
    if os.path.isfile(home+args.oaikey) is True:
        f = codecs.open(home+args.oaikey,encoding='UTF-8',mode='r')
        if f is not None:
            for line in f:
                if line != '\n' and line[0] != '#':
                    line = line.rstrip('\n')
                    gOpenAIKEY=line                   
            f.close()
        else:
            DB.error('OPEN AI key open fail, load fail')
    else :
        print('OPEN AI key doesn\'t existed, load fail')


def loadArgumentDb():
    global wordDb
    global cursor
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
    wordDb = sqlite3.connect(home+args.sql3db)
    cursor = wordDb.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS WOI
    (WORD TEXT PRIMARY KEY NOT NULL UNIQUE,
    REFCOUNT INT,
    NOTE_A TEXT,
    NOTE_B TEXT,
    NOTE_C TEXT
    );''')
    wordDb.commit()

def SQLStuff():
    global wordDb
    global cursor
    global tPage

    patterns = tPage.split("?p=")
    if len(patterns) > 1:
#        print(patterns[1])
        targetPattern = urllib.parse.unquote(patterns[1])
#        targetPattern = patterns[1].replace('%20',' ')
        cursor.execute(f"SELECT * FROM WOI WHERE WORD=\"{targetPattern}\"")
        rows = cursor.fetchall()
        rowsCnt = len(rows)
#        print(f"rows:{rowsCnt}")
        if rowsCnt == 0:
            cursor.execute(f"INSERT OR REPLACE INTO WOI(WORD,REFCOUNT) values(\"{targetPattern}\",1)")
            wordDb.commit()
        else:
            cursor.execute(f"UPDATE WOI SET REFCOUNT=REFCOUNT+1 WHERE WORD=\"{targetPattern}\"")
            wordDb.commit()
        
        cursor.execute(f"SELECT * FROM WOI WHERE WORD=\"{targetPattern}\"")
        for row in cursor.fetchall():
            print(f"This pattern : \"{row[0]}\" has been consulted {row[1]} times!")

def SQLFlush():
    global wordDb
    global cursor
    cursor.execute(f"DELETE FROM WOI")
    wordDb.commit()
    print("Gone in the wind...")

def SQLDump(mark=0):
    global wordDb
    global cursor
    global ScreenI
    rec_word = ""
    rec_cnt = 0
    rec_note_a = ""
    rec_note_b = ""
    rec_note_c = ""

    if mark == 0:
        cursor.execute(f"SELECT * FROM WOI")
    elif mark == 1:
        cursor.execute(f"SELECT * FROM WOI WHERE NOTE_A='M'")
    rows = cursor.fetchall()
    for row in rows:
        ScreenI.append({'word':row[0], 'refcnt':str(row[1]), 'note_a':str(row[2]), 'note_b':str(row[3]), 'note_c':str(row[4])})

    if len(rows) > 0:
        for x in range(85):
            print("=",end='')
        print("=")
        print("|"+clrTx("                                         Word","CYAN")+"|"+clrTx("Count","CYAN")+ \
        "|"+clrTx("      MARK","CYAN")+"|"+clrTx("    Note B","CYAN")+ \
        "|"+clrTx("    Note C","CYAN")+"|")
        for item in ScreenI:
            target_str = f"|{item['word']:>45}|{item['refcnt']:>5}|{item['note_a']:>10}|{item['note_b']:>10}|{item['note_c']:>10}|" 
            print(clrTx(target_str,"WHITE"))
        for x in range(85):
            print("=",end='')
        print("=")

def save_last_word(pattern):
    home = expanduser('~')
    f = open(home+args.database,'w')
    if f is not None:
        f.write(pattern+'\n')
    f.close()

def mark_last_word_a():
    global cursor
    global args
    home = expanduser('~')
    if os.path.isfile(home+args.database) is True:
        f = codecs.open(home+args.database,encoding='UTF-8',mode='r')
        if f is not None:
            for line in f:
                #print(f'check out:{line}\n')
                if line != '\n' and line[0] != '#':
                    line = line.rstrip('\n')
                    line = line.replace('%20',' ')
                    cursor.execute(f"SELECT * FROM WOI WHERE WORD=\"{line}\"")
                    rows = cursor.fetchall()
                    rowsCnt = len(rows)
                    if rowsCnt == 0:
                        print(f'target word \"{line}\" doesn\'t exist in the database')
                    else:
                        cursor.execute(f"UPDATE WOI SET NOTE_A='M' WHERE WORD=\"{line}\"")
                        wordDb.commit()
            f.close()
        else:
            DB.error('db file open fail')
    else :
        print('database doesn\'t existed')
    SQLDump(1)

def gen_close_test():
    global gOpenAIKEY
    global cursor
    
    loadOpenAIKey()
    if gOpenAIKEY=='':
        print('OPEN AI key doesn\'t existed, function abort.')
        exit(3)
 
    cursor.execute(f"SELECT * FROM WOI WHERE NOTE_A='M'")
    rows = cursor.fetchall()
    words_strings = []
    for row in rows:
        words_strings.append(row[0])

    words_string = ','.join(words_strings)

    openai.api_key=gOpenAIKEY
    openai.Model.list()

    #response = openai.Image.create(
    #        prompt="a black cat",
    #        n=1,
    #        size="1024x1024"
    #        )
    #image_url = response['data'][0]['url']
    #print(image_url)


    my_query="Could you generate a close test by using "+words_string+"?"
    
    print("ASK: "+my_query)

    response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Yout are a helpful assistant."},
#                {"role": "user", "content": "Could you generate a close test by using 'cat', 'dog', and 'hamster'?"}
#                {"role": "user", "content": "Could you generate an essay within 200 words by using 'cat', 'dog', and 'hamster'?"}
                {"role": "user", "content": my_query}
            ]
    )

    print(response['choices'][0]['message']['content'])


def main():
    global tPage
    global args
    global parser
    if args.statistic:
        SQLDump(0)
    elif args.listmark:
        SQLDump(1)
    elif args.flushdb:
        SQLFlush()
    elif args.marklastword is True:
        mark_last_word_a()
    elif args.doingAI:
        gen_close_test()
    elif not tPage or len(tPage) == 48:
        parser.print_help()
        exit(1)
    else:
        resultString = htmlParser(tPage)
        prettyPrint(resultString)
        SQLStuff()
        pattern = ' '.join(args.query)
        save_last_word(pattern)
            
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
    global parser
    global g_query_string_for_ai
    parser = argparse.ArgumentParser(description='A English Dictionary Utility with AI')
    parser.add_argument('-v', '--verbose', dest='verbose', action = 'store_true', default=False, help='Verbose mode')
    parser.add_argument('-d', '--database', dest='database', action = 'store', default='/.edict/edict.db')
    parser.add_argument('-q', '--sqlite3', dest='sql3db', action = 'store', default='/.edict/edict.db3')
    parser.add_argument('-s', '--statistic', dest='statistic', action = 'store_true', default=False, help='Dump all consult history')
    parser.add_argument('-l', '--listmark', dest='listmark', action = 'store_true', default=False, help='Dump all marked consult history')

    parser.add_argument('-f', '--flushdatabase', dest='flushdb', action = 'store_true', default=False, help='Flush database')
    parser.add_argument('-m', '--marklastword', dest='marklastword', action = 'store_true', default=False, help='mark last consulted word for further grouping')
    parser.add_argument('-a', '--ai', dest='doingAI', action = 'store_true', default=False, help='Doing AI base on consulting history')
    parser.add_argument('-i', '--queryai', dest='queryAI', action = 'store_true', default=False, help='Using AI to do something amazing')
    parser.add_argument('-k', '--openaikey', dest='oaikey', action = 'store', default='/.edict/.oaikey')

    parser.add_argument('query', nargs='*', default=None)
    args = parser.parse_args()
    if len(args.query) != 0:
        query_string = ' '.join(args.query)
        query_string = urllib.parse.quote(query_string)
        tPage = tPage+query_string
    log_level = logging.INFO
    if args.verbose:
        log_level = logging.DEBUG

if __name__ == '__main__':
    verify()
    loadArgumentDb()
    main()
    
