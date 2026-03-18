# 📖 Edict: AI-Powered Console Dictionary

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Edict** is a lightweight English-Chinese dictionary utility for the Linux console. Originally created in 2008 as a web crawler, it was modernized in 2023 with Generative AI to help users generate study materials like cloze tests. It is specifically designed for Traditional Chinese native speakers who use the Linux console or WSL.

---

## ✨ Key Features
* **Instant Lookup:** Crawls Yahoo Dictionary for KK/DJ/IPA phonetics and Traditional Chinese definitions.
* **Smart History:** Automatically tracks how many times you have consulted a specific word.
* **Favorites System:** "Mark" words to create a curated list for further study.
* **AI Study Assistant:** Uses OpenAI to generate custom **Cloze Tests** (fill-in-the-blank) based on your marked vocabulary.

---

## 🚀 Installation

### Prerequisites
* Python 3.x and Pip.
* A Linux environment (WSL/Ubuntu recommended).

### Setup
1. **Clone the repository:**
~~~bash
git clone <your-repository-link>
cd edict
~~~
2. **Run the installer:**
The script creates a virtual environment, installs dependencies (`beautifulsoup4`, `openai`), and sets up a hidden `.edict` folder in your home directory.
~~~bash
# For a full installation including database reset
./install.sh --full

# To update code while preserving your database
./install.sh
~~~

### 🤖 AI Configuration (Optional)
To use the generative study features, you need an OpenAI API key:
1. Obtain a key from OpenAI.
2. Save it to your config folder:
~~~bash
echo "your_open_ai_key" > .oaikey
mv .oaikey ~/.edict
~~~
*Note: You do not need an OpenAI key to use basic dictionary features.*

---

## 🛠 Usage Guide

### Basic Dictionary Lookup
Query a word directly from the console:
~~~bash
edict incantation
~~~
*Outputs: Phonetics, definitions from Yahoo/PyDict, and your consultation count.*

### Managing Vocabulary & History
* **View History (`-s`):** Displays a table of all consulted words and their counts.
* **Mark Last Word (`-m`):** Adds the most recently searched word to your favorites list.
* **List Marked (`-l`):** Dumps the list of all words you have marked.
* **Flush Database (`-f`):** Clears all history and marks.

### Generative AI Study Tool
Generate a cloze test from your marked words:
~~~bash
edict -a
~~~
**Example Output:**
> 1. The witch spoke a mysterious ________ that summoned a powerful spell.
> 2. The magician amazed the audience with his incredible ________ tricks.

---

## ⌨️ Command Options Summary

| Option | Description |
| :--- | :--- |
| `-h, --help` | Show the help message and exit |
| `-v, --verbose` | Enable verbose mode |
| `-s, --statistic`| Dump all consultation history |
| `-l, --listmark` | Show only marked (favorite) words |
| `-m, --marklastword` | Mark the last consulted word for further grouping |
| `-a, --ai` | Generate AI Cloze Test based on marked history |
| `-i, --queryai` | Using AI to do something amazing (custom queries) |
| `-f, --flushdatabase` | Clear all records from the database |
| `-k, --openaikey` | Manually provide an OpenAI key |

---

## 📺 Demo
Check out the usage guide video: [Watch on YouTube](https://www.youtube.com/watch?v=1uK9qrqCZDU).

## 🗺 Roadmap
- [ ] More generic AI features.
- [ ] Enhanced document reading support.
