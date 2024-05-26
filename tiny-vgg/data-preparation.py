from pathlib import Path
from os import chdir
path = './data'/ 'class_10_train' / 'n01882714' / 'images'  # The path to use
to_usenum = 0  # Start num
alltxt = list(path.glob('*.jpg'))  # Getting all the txt files
chdir(path)  # Changing the cwd to the path

for i, txtfile in enumerate(alltxt):
    to_usename = f"n01882714_{to_usenum+i}.JPEG"  # The name to use
    txtfile.rename(to_usename) 