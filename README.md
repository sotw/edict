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
|                                  incantation|    1|      None|      None|      None|
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

#### Feature: dump consulting history

```bash
> edict -s
======================================================================================
|                                         Word|Count|      MARK|    Note B|    Note C|
|                                       grease|    1|      None|      None|      None|
|                                           ai|    1|      None|      None|      None|
|                                   armageddon|    1|      None|      None|      None|
|                                     exoplnet|    1|      None|      None|      None|
|                                  incantation|    1|         M|      None|      None|
======================================================================================
```

#### Feature: dump the list of marked words

```bash
> edict -l
======================================================================================
|                                         Word|Count|      MARK|    Note B|    Note C|
|                                  incantation|    1|         M|      None|      None|
======================================================================================
```

#### Feature: Use generative AI to generate the close test with the list of marked words

This will take a while depending on the response time of OPEN AI. and you probably will get different result every time. I

```textile
> edict -a
ASK: Could you generate a close test by using incantation?
Certainly! Here's a close test using the theme of incantations:

Complete the following sentences by selecting the correct word or phrase:

1. In ancient rituals, the priest would recite a powerful _______ to invoke supernatural forces.
   a) mantra
   b) incantation
   c) spell
   d) enchantment

2. The ingredients for the magic potion included ___________, rare herbs, and a sprinkle of fairy dust.
   a) mystical crystals
   b) magical amulets
   c) arcane artifacts
   d) bewitched potions

3. As the wizard waved his wand and chanted the ________, the room filled with a shimmering aura.
   a) hex
   b) curse
   c) charm
   d) incantation

4. The witch carefully wrote down the intricate _______ for a powerful love spell.
   a) formula
   b) invocation
   c) enchantment
   d) mantra

5. The sorcerer's _______ echoed through the night, causing the earth to tremble and the sky to darken.
   a) mantra
   b) chant
   c) spell
   d) incantation

6. The fairy whispered a _______ to the newborn flower, instantly making it bloom with vibrant colors.
   a) spell
   b) incantation
   c) hex
   d) enchantment

7. The ancient book contained a collection of _______ from different cultures and civilizations.
   a) charms
   b) spells
   c) incantations
   d) mantras

8. The apprentices diligently practiced their _______ to master the art of spellcasting.
   a) enchantments
   b) incantations
   c) hexes
   d) rituals

9. The sorceress used her ________ to ward off evil spirits and protect the village from harm.
   a) incantation
   b) invocation
   c) mantra
   d) spell

10. The wise old wizard shared a secret ________ with the chosen hero, enabling them to defeat the dark sorcerer.
    a) enchantment
    b) incantation
    c) mantra
    d) invocation
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
