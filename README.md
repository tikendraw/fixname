# fixname
Removes Emojies from filenames

```
fire๐ฅ๐ฅ.png --> fire(emoji).png
hot๐๐.txt  --> hot(emoji).txt
```

# How to use
```
git clone https://github.com/tikendraw/fixname.git
cd fixname

usage: fixname.py [-h] [-d DIR] [-f FILE] [-r REPLACE]

This scripts removes emojies form filenames recursively.(ABSOLUTE PATH MUST BE GIVEN)

options:
  -h, --help              show this help message and exit
  -d DIR, --dir DIR       Directory containing files with emoji(s)
  -f FILE, --file FILE    Filename which contains emoji
  -r REPLACE, --replace   REPLACE
                          Replace the emojis with given word

```
