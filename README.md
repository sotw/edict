## Python3 English Dictionary

#### Introduction

This simple utility is actully my very first pet project. It's a really easy to use Chinese-English Dictionary web crawler. If you were a Traditional Chinese native speaker and a linux console user, this might be handy for you.

#### How to install

Need python3 and bs4 (beautifual soup 4)

1. git clone

2. install.sh

I will create a invisible .edict under your home folder

and place bashscript under $home/bin/sh

#### How to use

```bash
usage: edict.py [-h] [-v] [-d DATABASE] [-q SQL3DB] [-s] [-l] [-f] [-m] [query ...]

A English Dictionary Utility

positional arguments:
  query

options:
  -h, --help            show this help message and exit
  -v, --verbose         Verbose mode
  -d DATABASE, --database DATABASE
  -q SQL3DB, --sqlite3 SQL3DB
  -s, --statistic       Dump all consult history
  -l, --listmark        Dump all marked consult history
  -f, --flushdatabase   Flush database
  -m, --marklastword    mark last consulted word for further grouping#### Feature : auto record how many times you consult a word
```

```bash
edict -s
======================================================================================
|                                         Word|Count|      MARK|    Note B|    Note C|
|                                     fend off|    5|      None|      None|      None|
|                                     pump out|    4|      None|      None|      None|
|                                         pump|    4|      None|      None|      None|
|                                        plump|    4|      None|      None|      None|
|                                         evil|    3|      None|      None|      None|
|                                         live|    2|      None|      None|      None|
======================================================================================#### Feature : delete records
```

```bash
edict -f
Gone in the wind...
```

#### New Feature : mark the last word

```bash
edict test // make a consult
edict -s // dump to see the test is added (not necessary step)
======================================================================================
|                                         Word|Count|      MARK|    Note B|    Note C|
|                                     fend off|    5|      None|      None|      None|
|                                     pump out|    4|      None|      None|      None|
|                                         pump|    4|      None|      None|      None|
|                                        plump|    4|      None|      None|      None|
|                                         evil|    3|      None|      None|      None|
|                                         live|    2|      None|      None|      None|
|                                         test|    1|      None|      None|      None|
======================================================================================
edict -m //mark the last consulted word 'test'
======================================================================================
|                                         Word|Count|      MARK|    Note B|    Note C|
|                                         test|    1|         M|      None|      None|
======================================================================================
edict -l //to dump all work marked


```

This is a feature that mark word you think it worths to do it for any reason.

For example: you might think this is a word that you want to memory right after you consulted it. 



If you want to mark specific word, just consult it again and mark it.




