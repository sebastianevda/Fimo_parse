list_uniq = "pal_fino_unq.fa"

list_filename = "pal_fino_all.fa"

output_filename = "pal_fino_unq.fa.counts"

uniq = open(list_uniq)
listofnames = open(list_filename)
withmatchedid = open(output_filename, "w")
infile = open(list_filename)
read = infile.read()
read_u = uniq.read()
#cleaninfile = read.replace("\n","")
#rep = cleaninfile.replace (">","\n>")
splitrep = read.split("\n")

split_u = read_u.split("\n")

count = 0
for line in split_u:
    #print (line)
    for lines in splitrep:
        if line in lines:
            count = count + 1
    withmatchedid.write(line + "\t"+ str(count) + "\n")
    count = 0

withmatchedid.close()
