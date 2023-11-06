## An English Dictionary with AI

#Generative ai #Console English dictionary #web crawler

#### Introduction

This simple utility is actully my very first pet project back to 2008. It's a really easy to use English-Chinese Dictionary web crawler. If you were a Traditional Chinese native speaker and a linux console user, this might be handy for you.

At 2023, now I combined with AI usage.

Currently  you can use this simple utiliy to generate your own close test

#### How to install

Need python3 and bs4 (beautifual soup 4) and openai 

1. git clone

2. install.sh

I will create a invisible .edict under your home folder

and place bashscript under $home/bin/sh

###### [optional]

If you want to use  ai, you need to buy a openai key to use

google "open ai key"

Once you have the key, 

1. echo "my open ai key" > .oaikey

2. mv .oaikey ~/.edict

Note: you don't need to have openai key to use basic feature.

#### How to use

Check out the usage guide video: https://www.youtube.com/watch?v=1uK9qrqCZDU

Under console ( recommand wsl/ubuntu )

You can get a help file like the following:

```bash
> edict
usage: edict.py [-h] [-v] [-d DATABASE] [-q SQL3DB] [-s] [-l] [-f] [-m] [-a] [-i] [-k OAIKEY] [query ...]

A English Dictionary Utility with AI

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
  -m, --marklastword    mark last consulted word for further grouping
  -a, --ai              Doing AI base on consulting history
  -i, --queryai         Using AI to do something amazing
  -k OAIKEY, --openaikey OAIKEY
```

#### Feature: consult the chinese english dictionary

```bash
> edict incantation
search target:https://tw.dictionary.search.yahoo.com/search?p=incantation
KK[͵ɪnkænˋteʃən]
DJ[͵inkænˋteiʃən]
IPA[ˌɪnkænˈteɪʃn]
咒語
咒語
PyDict
This pattern : "incantation" has been consulted 1 times!
```

#### Feature: show consulting history

```bash
> edict -s

======================================================================================
|                                         Word|Count|      MARK|    Note B|    Note C|
|                                  incantation|    2|         M|      None|      None|
|                                        magic|    1|         M|      None|      None|
|                                          cat|    1|         M|      None|      None|
|                                          dog|    1|      None|      None|      None|
======================================================================================
```

#### Feature : mark the last word

Note: this utility will record the fail consulting string as well, so if you found a result is good enough for you. You can leave a mark for it, just like the **favorites list**.

```bash
> edict -m
======================================================================================
|                                         Word|Count|      MARK|    Note B|    Note C|
|                                  incantation|    1|         M|      None|      None|
====================================================================================== 
```

#### Feature: dump the list of marked words

```bash
> edict -l
======================================================================================
|                                         Word|Count|      MARK|    Note B|    Note C|
|                                  incantation|    2|         M|      None|      None|
|                                        magic|    1|         M|      None|      None|
|                                          cat|    1|         M|      None|      None|
======================================================================================
```

#### Feature: Use generative AI to generate the close test with the list of marked words

This will take a while depending on the response time of OPEN AI. and you probably will get different result every time. I

```textile
> edict -a
ASK: Could you generate a close test by using incantation,magic,cat?
Certainly! Here's a close test using the words "incantation," "magic," and "cat":

1. The witch spoke a mysterious ________ that summoned a powerful spell.
2. The magician amazed the audience with his incredible ________ tricks.
3. The ancient book contained secret ________ spells handed down through generations.
4. The little girl giggled as she watched her ________ playfully chase a ball of yarn.
5. The sorcerer waved his wand and whispered an ________ to make the object levitate.
6. The old wizard had a black ________ that seemed to possess mystical powers.
7. The enchantress used an ________ to transform a pumpkin into a beautiful carriage.
8. The charmed amulet radiated a pulsating ________ energy.
9. The feline companion purred contentedly as the witch recited a poetic ________.
10. The illusionist's breathtaking ________ show left the audience in awe.

Remember to fill in the blanks with the most suitable word that fits the context.
```

#### Feature empty the history

This simple utility is designed for reading a document once a time currently.

So you might want to empty the record at ceratin point.

```bash
> edict -f
Gone in the wind...
```

To do:

More generic ai feature. It's amazing
