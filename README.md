# fixname  : Remove Emoji from Filenames
This Python script removes emojis from filenames.

## Usage
The script can be run from the command line using the following arguments:

```
python fixname.py -d /path/to/directory/with/files
python fixname.py -f /path/to/single/file/with/emoji😀.png
```
The -d option is used to specify the directory that contains files with emojis in their names. The -f option is used to specify a single file with an emoji in its name.

By default, the script replaces the emojis with the string (emoji). However, you can use the -r option to specify a different string to replace the emojis with:

```
python fixname.py -d /path/to/directory/with/files -r _emoji_
```

## Dependencies
This script requires the tqdm and colorama libraries to be installed. You can install them using pip:

```
pip install tqdm colorama
```

## Emoji Removal Algorithm
The algorithm used to remove the emojis from filenames is based on the regular expression pattern in the remove_emoji() function. The pattern matches a wide range of Unicode characters that represent emojis, symbols, and pictographs. When the pattern finds a match in the filename, it replaces the emoji with the string specified by the user.

## Limitations
The script only removes emojis from filenames, not from file contents. It also does not handle non-Unicode character encodings, such as ASCII or ISO-8859-1.

## License
This script is licensed under the MIT License.
