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
edict [word]
```

```bash
usage: edict.py [-h] [-v] [-d DATABASE] [-q SQL3DB] [-s] [-f] [query ...]

A English Dictionary Utility

positional arguments:
  query

options:
  -h, --help            show this help message and exit
  -v, --verbose         Verbose mode
  -d DATABASE, --database DATABASE
  -q SQL3DB, --sqlite3 SQL3DB
  -s, --statistic       Some statistic
  -f, --flushdatabase   Flush databaseme statistic
```

#### New Feature : auto record how many times you consult a word

```bash
edict -s
======================================================================================
|                                         Word|Count|    Note A|    Note B|    Note C|
|                                     fend off|    5|      None|      None|      None|
|                                     pump out|    4|      None|      None|      None|
|                                         pump|    4|      None|      None|      None|
|                                        plump|    4|      None|      None|      None|
|                                         evil|    3|      None|      None|      None|
|                                         live|    2|      None|      None|      None|
======================================================================================
```

#### New Feature : delete records

```bash
edict -f
Gone in the wind...
```


