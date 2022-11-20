
#!/usr/bin/env python
"""
Remove emoji from a text file and print it to stdout.
Usage
-----
    python remove-emoji.py input.txt > output.txt
"""
import re
import pandas as pd
import sys
import os
# https://stackoverflow.com/a/49146722/330558
from tqdm import tqdm
from colorama import Fore, Back, Style

def remove_emoji(string):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002500-\U00002BEF"  # chinese char
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f"  # dingbats
                               u"\u3030"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'(emoji)', string)


# RETURNS FILENAMES
def dir_walkthrough(path):
    '''
    shows the contents of the file directory
    '''
    all_filenames = []	

    for dirname, _ , files in os.walk(path):
        all_filenames += [os.path.join(dirname, file) for file in files]

    return all_filenames

def name_change(full_file_name):
	dir,old_name = os.path.split(full_file_name)
	new_name = remove_emoji(old_name)

	if old_name != new_name:
		os.rename(os.path.join(dir,old_name), os.path.join(dir,new_name) )
		print(Fore.GREEN + f'Renamed: {old_name} --> {new_name}')
	else:
		# print(old_name)
		pass

if __name__ == '__main__':

	directory = sys.argv[1]

	if sys.argv[1] in ['-h', '--help']:
		print('python3 fixname.py [dirname]')

	elif os.path.exists(directory):
		pass
	else:
		directory = input('Enter the Directory : ')
	
	print(directory)

	all_files = dir_walkthrough(directory)

	for name in tqdm(all_files):
		name_change(full_file_name = name)



