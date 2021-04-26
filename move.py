import os
import shutil

# Change current directory 
os.chdir("/home/marquez/Downloads")
put = os.listdir("/home/marquez/Downloads")

# Get current directory
current = os.getcwd()

# Destination directory
dest = "/home/marquez/Pictures"

countJpg = 0  
my_list = []      

slikaJpg = ".jpg"
slikaPng = ".png"

for p in put:

	if p.endswith(slikaJpg) or p.endswith(slikaPng):

		print(p)
		shutil.move(p, dest)




