import textwrap as tw
import sys
import re
title=input("Book Title")
filename = input("name for the files, prolly just the title sans spaces")

def splitn(input_list,n):
    return [input_list[i:i+n] for i in range(0, len(input_list), n)]

with open(sys.argv[1], 'r') as infile:

	workingfile = infile.read()

linelst = tw.wrap(workingfile, width=19)
pagelst = splitn(linelst,13)
vlmelst = splitn(pagelst,100)
print(len(vlmelst))

n="\n"
v=1
for volume in vlmelst:
	entry = open("./" + filename +"vol" + str(v) + ".stendhal", "w")
	entry.write("title: "+title+"vol"+str(v)+n)
	entry.write("author: TheSquashy"+n)
	entry.write("pages:"+n)
	for page in volume:
		i=0
		for line in page:
			if i == 0:
				entry.write("#- "+str(line)+n)
			else:
				entry.write(line+n)
			i +=1
	entry.close()
	v+=1
