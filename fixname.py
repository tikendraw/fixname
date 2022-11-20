
#!/usr/bin/env python
"""
Remove emoji from filnames
Usage
-----
	# python fixname.py -d /home/user/Downloads
	# python fixname.py -f /home/user/somefile🔥💋.png
"""
import re
import pandas as pd
import argparse
import sys
import os
# https://stackoverflow.com/a/49146722/330558
from tqdm import tqdm
from colorama import Fore, Back, Style

def remove_emoji(string,replace_with = 'emoji'):
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
	return emoji_pattern.sub(fr'{replace_with}', string)


# RETURNS FILENAMES
def dir_walkthrough(path):
	'''
	shows the contents of the file directory
	'''
	all_filenames = []	

	for dirname, _ , files in os.walk(path):
		all_filenames += [os.path.join(dirname, file) for file in files]

	return all_filenames

def name_change(full_file_name, replace_with):
	dir,old_name = os.path.split(full_file_name)
	new_name = remove_emoji(old_name,replace_with)

	if old_name != new_name:
		os.rename(os.path.join(dir,old_name), os.path.join(dir,new_name) )
		print(Fore.GREEN + f'Renamed: {old_name} --> {new_name}')
	else:
		# print(old_name)
		pass

if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='This scripts removes emojies form filenames recursively.(ABSOLUTE PATH MUST BE GIVEN)')
	parser.add_argument('-d','--dir', type=str, help='Directory containing files with emoji(s)', required=False)
	parser.add_argument('-f','--file', type=str, help='Filename which contains emoji', required=False)
	parser.add_argument('-r','--replace', type=str, help='Replace the emojis with given word', required=False)

	args = vars(parser.parse_args())
	
	# print('dirname',args['dir'],'\nfilename:',args['file'])
	
	if args['replace']:
		replace_with = args['replace']
		print(replace_with)
	else:
		replace_with = '(emoji)'

	if args['dir']:
		dirname = args['dir']

		
		if os.path.isdir(dirname):
			all_files = dir_walkthrough(dirname)
			print(len(all_files))

			for name in tqdm(all_files):
				name_change(full_file_name = name,replace_with=replace_with)
		else:
			print("directory doesn't exists")

	if args['file']:

		filename = args['file']
		if os.path.isfile(filename):
			name_change(full_file_name = filename, replace_with=replace_with)	
		else:
			print("file doesn't exists")

		



